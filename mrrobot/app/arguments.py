import argparse

def parse():
    # Name and description
    parser = argparse.ArgumentParser(
        prog="mrrobot",
        description="A robot to automate the hacking process",
        add_help=True)
    # ---- Information
    information = parser.add_argument_group(title="information")
    # Version
    information.add_argument(
        "--version",
        action="version",
        version="MrRobot v1.0.0",
        help="Print the version")
    # ---- Challenge
    challenge = parser.add_argument_group(title="challenge")
    # Input (Challenge)
    challenge.add_argument(
        "input",
        type=str,
        metavar="CHALLENGE",
        help="Challenge input (Can be a string or a file)")
    # Inside flag
    challenge.add_argument(
        "--inside",
        action="store_true",
        help="Solve in-flag challenges. Option -u/--unit must be used"
    )
    # Find all flag
    challenge.add_argument(
        "--find-all",
        action="store_true",
        help="Find all possible flags, no just the first"
    )
    # Flag format
    challenge.add_argument(
        "-f", "--flag",
        metavar="FLAG",
        action="store",
        help="Specify the regex-based flag format (Default: MrRobotCTF{.*})")
    # Flag format
    challenge.add_argument(
        "--safe",
        action="store_true",
        help="Specify to avoid units that generate false positives")
    # ---- Performance
    performance = parser.add_argument_group(title="configuration")
    # Clean
    performance.add_argument(
        "--clean",
        action="store_true",
        help="Remove the default configuration if exists")
    # File (Configuration)
    performance.add_argument(
        "-c", "--config",
        dest="config",
        metavar="INI",
        action="store",
        help="Specify the configuration file (Default: mrrobot.ini)")
    # Banner
    performance.add_argument(
        "--no-banner",
        action="store_true",
        help="Hide the banner")
    # Coding
    performance.add_argument(
        "--encoding",
        type=str,
        metavar="CODING",
        help="Set the encoding method (Default: utf-8)")
    # Timeout
    performance.add_argument(
        "--timeout",
        type=float,
        metavar="SECONDS",
        help="Set the timeout to the specified number of seconds (Default: 10. Disabled: 0)")
    # ---- Units Group
    units = parser.add_argument_group(title="available categories")
    # All
    units.add_argument(
        "-a", "--all",
        action="store_true",
        help="Load all units (Default)"
    )
    # Only one unit
    units.add_argument(
        "-u", "--unit",
        type=str,
        action="store",
        help="Load an specific unit (Format: category.unit)"
    )
    # ------- Categories
    # Crypto
    units.add_argument(
        "--crypto",
        action="store_true",
        help="Load crypto units"
    )
    # Esoteric
    units.add_argument(
        "--esoteric",
        action="store_true",
        help="Load esoteric units"
    )
    # Forensics
    units.add_argument(
        "--forensics",
        action="store_true",
        help="Load forensics units"
    )
    # Parse the arguments
    return parser.parse_args()