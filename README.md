# game-dev-math

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

- `pip install jupyterlab` - install (migrate both commands to conda)
- `pip install jupyterlab-latex` - install LaTeX support (Doesn't work?)
- [NbConverter](https://saturncloud.io/blog/how-to-use-latex-in-jupyter-notebook/) works better
- `jupyter labextension list` - list all the plugins
- `jupyter lab --no-browser` - start

Additional requirements:
- [Quarto](https://quarto.org/docs/get-started/) for preview

### Result

Pros:
- Works well
- Instant visualization
- LaTeX support
- Popular
- Many handy tools

Cons:
- A lot of soft and plugins to install
- Runs in browser
- Not very convenient on the first look

## Latex

### Overleaf

Just a web pure LaTeX editor with subscription

### TexMaker

Pure LaTeX editor

### TODO: start from playing with Manim

>Test LaTeX
 
$$P \left( A=2 \, \middle| \, \dfrac{A^2}{B}>4 \right)$$
