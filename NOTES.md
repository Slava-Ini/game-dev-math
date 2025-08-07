# Notes

## Documenting Tool Options

1. [Jupiter Lab + LaTeX converter + Preview](#jupiter-lab)
2. [Wolfram](https://www.wolfram.com/mathematica/)
3. [Mainm](https://docs.manim.community/en/stable/guides/using_text.html#text-with-latex)
4. LaTeX text editors
     - [Overleaf](https://www.overleaf.com/)
     - [TexMaker](https://www.xm1math.net/texmaker/index.html)
     - [TexLap - LSP](https://github.com/latex-lsp/texlab)
     - [Vimtex - Vim LSP](https://github.com/lervag/vimtex)
5. Visualizers
     - [Desmos](https://www.desmos.com/geometry/tjtt82sxwi)
     - [GeoGebra](https://www.geogebra.org/math/angles#upper-elementary)

## Jupiter Lab

### Installation

- `pip install jupyterlab-latex` - install LaTeX support (Doesn't work?)
- [NbConverter](https://saturncloud.io/blog/how-to-use-latex-in-jupyter-notebook/) works better

Additional requirements:
- [Quarto](https://quarto.org/docs/get-started/) for preview

## Latex

### Overleaf

Just a web pure LaTeX editor with subscription

### TexMaker

Pure LaTeX editor

## Manim

Library for making videos, images and gifts
Generally not usable on it's own, has some troubles with running on WSL smoothly
Long compile times, however worth trying within Markdown or Jupyter

## Commands

- Switch conda env `conda activate my-manim-environment`

## Plan

- Another option is to use Markdown as it supports LaTeX and we can still paste Manim stuff there


## Next steps

- Try to describe PoP problem using JL
- ! Take a closer look at [pip-tools](https://github.com/jazzband/pip-tools) to better manage the dependencies
- ! Learn more about `pyproject.toml`
