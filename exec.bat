@echo off
REM Ottieni il percorso della directory in cui si trova il file batch
set SCRIPT_DIR=%~dp0

REM Cambia directory alla cartella contenente il file Main.py
cd /d "%SCRIPT_DIR%"

REM Esegui il file Main.py con Python
python Main.py

REM Pausa per mantenere la finestra del prompt dei comandi aperta dopo l'esecuzione
pause
