@echo off
echo Compiling Goldbach Conjecture Survey...
echo.

echo Step 1: Running pdflatex...
pdflatex -interaction=nonstopmode main.tex

echo Step 2: Running bibtex...
bibtex main

echo Step 3: Running pdflatex (second pass)...
pdflatex -interaction=nonstopmode main.tex

echo Step 4: Running pdflatex (third pass)...
pdflatex -interaction=nonstopmode main.tex

echo.
echo Compilation complete!
echo Output: main.pdf
pause
