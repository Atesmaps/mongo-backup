# MongoDB Backup Tool

An Atesmaps tool to back up Mongo database and upload
dump files to DigitalOcean spaces.

## Deploy

This project uses GitHub Actions for manage deployments.
See [deploy.yaml](.github/workflows/deploy.yaml) for more details.

## Local Development

This project requires `Python3`.

#### Steps

1. Install `pipenv`:
    ```bash
    pip install --upgrade pip && pip install pipenv
    ```
2. Activate virtualenv:
    ```bash
    pipenv shell
    ```
3. Run Python script:
    ```bash
    python src/main.py
    ```

## Collaborators
- Nil Torrano: <ntorrano@atesmaps.org>
- Atesmaps: <info@atesmaps.org>
