#!/usr/bin/env python3

"""
Injects LED control commands into the OPNsense ppp up and down scripts
Uses https://github.com/stephenw10/WGXepc to control the LEDs on a Firebox

Copy to /usr/local/etc/rc.syshook.d/early/20-injectWGXepc and chmod to 755
"""

ScriptPath = "/usr/local/opnsense/scripts/interfaces/"  # Path to ppp-scripts
upScript = ScriptPath + "ppp-linkup.sh"  # ppp-linkup script name with path
upLine = "WGXepc64 -l green\n"  # line to insert into up script
downScript = ScriptPath + "ppp-linkdown.sh"  # ppp-linkdown script name with path
downLine = "WGXepc64 -l red\n"  # line to insert into down script

nextLine = "exit 0\n"  # line to look for to find inject-position


def inject(script: str, line: str, nextline: str = nextLine) -> None:
    """
    Checks if line is in script and inserts it before nextline if not

    :param script:
    Path to the script
    :param line:
    Line to insert into the script
    :param nextline:
    Line to look for to find inject-position
    :return:
    None
    """
    with open(script, "r") as f:
        lines = f.readlines()
    if line not in lines:
        print(f"Inserting {line} into {script}")
        lines.insert(lines.index(nextline), line)
        with open(script, "w") as f:
            f.writelines(lines)
    else:
        print(f"{line} already found in {script}")


def main():
    inject(upScript, upLine)
    inject(downScript, downLine)


if __name__ == "__main__":
    main()
