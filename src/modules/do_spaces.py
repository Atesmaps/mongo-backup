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
import logging
from datetime import datetime
from os import getenv, listdir

import boto3
from botocore.client import ClientError

logger = logging.getLogger()


class Spaces:
    def __init__(self):
        self.session = self.get_session()

    @staticmethod
    def get_session() -> boto3.session:
        """Connection with DigitalOcean spaces."""
        try:
            return boto3.session.Session().client(
                "s3",
                region_name=getenv("SPACES_REGION"),
                endpoint_url=getenv("SPACES_ENDPOINT"),
                aws_access_key_id=getenv("SPACES_ACCESS_KEY"),
                aws_secret_access_key=getenv("SPACES_SECRET_ACCESS_KEY"),
            )
        except ClientError as exc:
            raise Exception("Couldn't connect with DigitalOcean spaces.") from exc

    def upload_backup(self, backup_dir: str) -> None:
        """Upload a backup files to DigitalOcean spaces."""
        try:
            logger.info(f"Uploading backup files to DigitalOcena Spaces...")
            backup_timestamp = datetime.now().strftime(
                "%Y%m%d%H%M"
            )  # Format: YYYYmmddHHMM

            for f in listdir(path=backup_dir):
                logger.info(f"Uploading file {f!r}...")
                self.session.upload_file(
                    f"{backup_dir}/{f}",
                    "mongodb",
                    f"{backup_timestamp[:-6]}/{backup_timestamp[:-4]}/{f}",
                )
            logger.info("Backup files uploaded successfully.")
        except ClientError as exc:
            raise Exception("An error occurred uploading backup file.") from exc
