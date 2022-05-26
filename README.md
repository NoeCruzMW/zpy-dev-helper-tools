# ZPy Development Helper Tools

Scripts, function etc.

## Getting Started

Clone this repository for local deploy.

### Prerequisites

- python3.9

### Installing

- Create virtual environment, activate it and download all dependencies.

```bash
  virtualenv venv
```

- Clone repository

```bash

git clone https://github.com/NoeCruzMW/zpy-dev-helper-tools.git

```

## Actions

Upload config.json

```bash
{
  "user": "Noe Cruz",
  "sender": {
    "bid": "-",
    "cid": 610090982,
  },
  "actions": {
    "public_ip_request_action": {
      "execute": true,
      "sender": true,
      "data": {
        "message": "Hola equipo, me ayudan a configurar la sig. ip para conectar a la VPN de dev por favor.",
        "raw": {
          "user": "noe.cruz",
          "ip": ""
        }
      }
    }
  }
}


```

Run action

```bash
python actions_executor.py
```

Or from shell

`````shell
# For windows
./run_action_win.bat
`````

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see
the [tags on this repository](https://git-codecommit.us-east-1.amazonaws.com/v1/repos/redsocial-ws-ms-friend-request-sender/CHANGELOG.md)
.

## Authors

- **Noé Cruz** - _[Backend Developer](https://www.linkedin.com/in/zurckz/)_
