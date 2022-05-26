from typing import Any, Dict, Optional
import urllib.request
import json

config: Optional[Dict[Any, Any]] = None


def setup_config(config_: Dict[str, Any]) -> None:
    global config
    config = config_


def sender(content: str) -> Any:
    global config
    config = config.get("sender", {})
    url = f"https://api.telegram.org/{config.get('bid')}/sendMessage?chat_id={config.get('cid')}&parse_mode=html&text={content}"
    return urllib.request.urlopen(url.replace(" ", "%20")).read().decode("utf8")


def run(action, params, k) -> Any:
    current_config = params["actions"][k]
    if "execute" in current_config and not current_config["execute"]:
        return
    res = action(current_config["data"], params["user"])
    if "sender" in current_config and current_config["sender"] is True:
        res = sender(res)
    print(f"{k} action executed successfully ✅")
    return res


def public_ip_request_action(data: dict, user: str) -> str:
    ip = urllib.request.urlopen("https://ident.me").read().decode("utf8")
    raw = data.get("raw")
    raw["ip"] = ip
    return f"""<b><strong>{user}</strong></b>%0A%0A{data.get('message')}%0A%0A<b><code>{json.dumps(raw)}</code></b>%0A"""
