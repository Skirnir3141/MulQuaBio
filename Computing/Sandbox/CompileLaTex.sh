#!/bin/bash
pdflatex $1.tex
bibtex $1
pdflatex $1.tex
pdflatex $1.tex
echo $1 | cut -d '.' -f 1 | evince $1.pdf &

## Cleanup
rm *.aux
rm *.log
rm *.bbl
rm *.blg
