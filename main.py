import argparse
import logging
import pathlib
import re

logger = logging.getLogger(__name__)


def setup_logging(verbosity: int) -> None:
    """Configure logging based on verbosity level."""
    levels = [logging.WARNING, logging.INFO, logging.DEBUG]
    level = levels[min(verbosity, len(levels) - 1)]
    logging.basicConfig(
        format="%(levelname)s: %(message)s",
        level=level,
    )


def escape_files(
    start_dir: pathlib.Path,
    pattern: str,
    old_delim: str,
    new_delim: str,
) -> None:
    """Escape delimiters in txtar files."""
    regex = re.compile(
        rf"^{re.escape(old_delim)}\s+(.+?)\s+{re.escape(old_delim)}$",
        flags=re.MULTILINE,
    )
    replacement = rf"{new_delim} \1 {new_delim}"

    for path in start_dir.rglob(pattern):
        logger.info("Processing %s", path)
        content = path.read_text()
        new_content = regex.sub(replacement, content)

        if new_content != content:
            _ = path.write_text(new_content)
            logger.debug("Modified %s", path)


def unescape_files(
    start_dir: pathlib.Path,
    pattern: str,
    old_delim: str,
    new_delim: str,
) -> None:
    """Unescape delimiters in txtar files."""
    regex = re.compile(
        rf"^{re.escape(new_delim)}\s+(.+?)\s+{re.escape(new_delim)}$",
        flags=re.MULTILINE,
    )
    replacement = rf"{old_delim} \1 {old_delim}"

    for path in start_dir.rglob(pattern):
        logger.info("Processing %s", path)
        content = path.read_text()
        new_content = regex.sub(replacement, content)

        if new_content != content:
            _ = path.write_text(new_content)
            logger.debug("Modified %s", path)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Escape/unescape delimiters in txtar files"
    )
    _ = parser.add_argument(
        "command",
        choices=["escape", "unescape"],
        help="Command to execute",
    )
    _ = parser.add_argument(
        "--dir",
        type=pathlib.Path,
        default=pathlib.Path(),
        help="Starting directory (default: .)",
    )
    _ = parser.add_argument(
        "--pattern",
        default="*.txtar",
        help="File pattern to match (default: *.txtar)",
    )
    _ = parser.add_argument(
        "--old-delim",
        default="--",
        help="Original delimiter (default: --)",
    )
    _ = parser.add_argument(
        "--new-delim",
        default="@@",
        help="Replacement delimiter (default: @@)",
    )
    _ = parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Increase verbosity (-v, -vv, -vvv)",
    )

    args = parser.parse_args()
    setup_logging(args.verbose)

    if args.command == "escape":
        escape_files(args.dir, args.pattern, args.old_delim, args.new_delim)
    else:
        unescape_files(args.dir, args.pattern, args.old_delim, args.new_delim)


if __name__ == "__main__":
    main()
