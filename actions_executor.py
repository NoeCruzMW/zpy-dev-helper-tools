from zpy.actions import setup_config, run, public_ip_request_action
import json

actions = {"public_ip_request_action": public_ip_request_action}

if __name__ == "__main__":
    with open("./config.json", mode="r") as raw:
        config = json.loads(raw.read())
    setup_config(config)
    [run(actions[k], config, k) for k in config.get("actions").keys() if k in actions]
