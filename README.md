# CPS 310 Support Ticket Summary

This starter project is used for the Containers & Continuous Integration ICA.

## What the Program Does

The program:

- loads settings from `config.json`
- reads ticket data from `tickets.csv`
- counts total tickets
- counts open tickets
- counts high-priority tickets
- prints a summary to the terminal

## Requirements

- Python 3.12 or newer
- Git

Install dependencies with:

```text
python -m pip install -r requirements.txt
```

## Run the Program

### Windows

```text
python app.py
```

### macOS

```text
python3 app.py
```

## Run the Tests

### Windows

```text
python -m pytest -v
```

### macOS

```text
python3 -m pytest -v
```

## Important

This starter project intentionally does **not** include:

```text
Dockerfile
.dockerignore
.github/workflows/tests.yml
```

You will create those during the ICA.
