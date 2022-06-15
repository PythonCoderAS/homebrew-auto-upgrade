from asyncio import create_subprocess_exec, create_task, gather, run
from asyncio.subprocess import DEVNULL
from re import compile

from aioconsole import ainput, aprint

# https://stackoverflow.com/a/14693789/12248328
ansi_escape = compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
log_file = open("bump.log", "a", encoding="utf-8")


async def bump_item(item: str):
    log_file.write(item + "\n")
    await create_subprocess_exec("brew", "bump", "--open-pr", item, stdin=DEVNULL, stdout=DEVNULL, stderr=DEVNULL)


def filter(line: str) -> bool:
    return "==> " in line and line.split("==> ")[1].strip().startswith("\x1b[32m")


async def main():
    tasks = []
    try:
        while text := await ainput():
            if not filter(text):
                continue
            else:
                package = ansi_escape.sub('', text.split(": ")[0].strip())
                tasks.append(create_task(bump_item(package)))
    except EOFError:
        # We're done.
        pass
    finally:
        await gather(*tasks)


if __name__ == '__main__':
    run(main())
