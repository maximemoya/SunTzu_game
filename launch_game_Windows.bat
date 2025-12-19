@echo off
REM Script de lancement pour SunTzu Game (Windows)
REM Ce script active l'environnement virtuel et lance le jeu

echo =======================================
echo     Lancement de SunTzu Game
echo =======================================
echo.

REM Se deplacer dans le repertoire du script
cd /d "%~dp0"

REM Verifier si l'environnement virtuel existe
if not exist "venv\" (
    echo [ERREUR] Environnement virtuel non trouve!
    echo Creation de l'environnement virtuel...
    python -m venv venv

    if errorlevel 1 (
        echo [ERREUR] Erreur lors de la creation du venv
        pause
        exit /b 1
    )

    echo [OK] Environnement virtuel cree

    REM Activer l'environnement et installer les dependances
    echo Installation des dependances...
    call venv\Scripts\activate.bat
    pip install -r requirements.txt

    if errorlevel 1 (
        echo [ERREUR] Erreur lors de l'installation des dependances
        call venv\Scripts\deactivate.bat
        pause
        exit /b 1
    )

    echo [OK] Dependances installees
) else (
    REM Activer l'environnement virtuel existant
    echo Activation de l'environnement virtuel...
    call venv\Scripts\activate.bat
    echo [OK] Environnement virtuel active
)

REM Se deplacer dans le dossier du jeu
cd "SunTzuV01_BETA"

REM Lancer le jeu
echo.
echo Lancement du jeu...
echo =======================================
echo.
python main.py

REM Capturer le code de sortie
set GAME_EXIT_CODE=%errorlevel%

REM Retourner au repertoire racine
cd ..

REM Desactiver l'environnement virtuel
call venv\Scripts\deactivate.bat

echo.
echo =======================================
if %GAME_EXIT_CODE% equ 0 (
    echo [OK] Jeu termine normalement
) else (
    echo [ERREUR] Le jeu s'est termine avec une erreur (code: %GAME_EXIT_CODE%^)
)
echo =======================================
echo.

pause
exit /b %GAME_EXIT_CODE%
