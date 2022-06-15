# homebrew-auto-upgrade
Automatically upgrade applicable packages based on `brew livecheck --all`.

## How to use

1. Install `expect` via homebrew: `brew install expect`
2. Run `unbuffer -p brew livecheck`
3. Pipe output to this script

Example command:

```shell
unbuffer -p brew livecheck --all | pipenv run python main.py
```
