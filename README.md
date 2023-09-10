# Overview

This is a sample Restaurant api application using Python

# Set Up

Install [Pyenv](https://github.com/pyenv/pyenv) following the [official installation instructions](https://github.com/pyenv/pyenv#installation).

Download the proper python version:

```bash
# Installs the version from ".python-version" if not installed 
# Can take some time.
pyenv install
```

Install pipenv:

```bash
pip install --user pipenv
```

Install all dependencies

```bash
pipenv install
```

# Run locally

```bash
# If you haven't already, then start a pipenv shell
pipenv shell

PYTHON_ENV=development python src/main.py
```

Visit Swagger UI on [http://localhost:5000/api/swagger](http://localhost:5000/api/swagger).

# Run unit tests


```bash
# If you haven't already, then start a pipenv shell
pipenv shell

python -m pytest
```

## Test with Clients

Run the server

Open another shell and run the client:

```
python client/client.py
```

## API Design

Visit Swagger UI on [http://localhost:5000/swagger](http://localhost:5000/swagger).

## License

MIT