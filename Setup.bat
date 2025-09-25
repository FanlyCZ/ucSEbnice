@ECHO OFF

REM Vytvoření virtuálního prostředí v adresáři .venv
python -m venv .venv

REM Aktivace virtuálního prostředí
CALL .venv\Scripts\activate.bat

REM Instalace knihoven ze souboru requirements.txt
pip install -r requirements.txt

ECHO Virtual environment was created and packages installed.
PAUSE