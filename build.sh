#!/bin/bash

source .venv/bin/activate # linux
# .venv\Scripts\activate # win

pyinstaller --onefile \
            --name nx-pallete \
            --console \
            main.py

cp ./dist/nx-pallete ~/.local/bin/
cp ./colors.txt ~/.local/share/nx-pallete/
cp ./colors.txt ./dist/colors.txt
