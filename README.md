# Game Dev Math

This repository contains some insights on game dev related math
It's a series of Jupyter Lab notes on different topics with visualisations

## Contents

- [Setup](#setup)
- [Commands](#commands)

## Setup

- Create a virtual environment `python3 -m venv jupyter`
- Activate an environment `source jupyter/bin/activate.fish`
- Register an environment in Jupyter Lab
```sh
python -m ipykernel install --user --name=math-notes --display-name "Math Notes"
```
- Install the dependencies `pip install -r requirements.txt`
- Start Jupyter Lab `jupyter lab`
- Select the `Math Notes` kernel

## Commands

### Python

- `pip show <package_name>` - display the version of the package installed in the environment
- `pip freeze > requirements.txt` - update dependencies file in case of installing new ones

### Jupyter Lab

- `jupyter labextension list` - list all the plugins
- `jupyter lab --no-browser` - start headless

## TODO

- Configure the shortcuts for code collapsing according to the [post](https://stackoverflow.com/questions/49280261/jupyter-lab-shortcuts)
- Improve `requirements.txt`
