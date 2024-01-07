#!/usr/bin/env python3
######################################################
#
#   ** Atesmaps - MongoDB Backups **
#
#   An Atesmaps tool to back up MondoDB data and
#   unpload dump to DigitalOcean Spaces.
#
#   Collaborators:
#     - Nil Torrano: ntorrano@atesmaps.org
#     - Atesmaps Team: info@atesmaps.org
#
#   January 2024
#
######################################################
from os import getenv

from modules.do_spaces import Spaces
from modules.mongo import Mongo

OUTPUT_DIR = f"/tmp/{getenv('MONGO_DATABASE')}"


def create_dir(directory: str) -> None:
    """Assert output path exists."""
    from pathlib import Path

    Path(directory).mkdir(parents=True, exist_ok=True)


def main() -> None:
    """Backup Mongo database."""

    # Create output directory
    create_dir(directory=OUTPUT_DIR)

    # Do backup
    Mongo().do_backup(output_path=OUTPUT_DIR)

    # Upload to DigitalOcean
    Spaces().upload_backup(backup_dir=OUTPUT_DIR)


if __name__ == "__main__":
    main()
