# Game Dev Math

This repository contains some insights on game dev related math
It's a series of Jupyter Lab notes on different topics with visualisations

## Contents

- [Setup](#setup)
- [Commands](#commands)

## Setup

- Create a virtual environment `python3 -m venv jupyter`
- Activate an environment `source jupyter/bin/activate.fish`
- Install the dependencies `pip install -r requirements.txt`
- Register an environment in Jupyter Lab
```sh
python -m ipykernel install --user --name=math-notes --display-name "Math Notes"
```
- Start Jupyter Lab `jupyter lab`
- Select the `Math Notes` kernel (May already be selected automatically)

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
- Install Pandoc and other [requirements](https://stackoverflow.com/questions/29156653/ipython-jupyter-problems-saving-notebook-as-pdf) to be able to save `.pdf`
- Sort all the math notes
- Think what to do with chunky `.pdf`s


## To Learn:

- Binominal theorem for $(a-b)^2 = a^2-2ab-b^2$
- Laplass Expansion to understand determinant formula better
- More on [matrix transpose](https://www.youtube.com/watch?v=g4ecBFmvAYU)
