#!/bin/zsh

# Script de lancement pour SunTzu Game
# Ce script active l'environnement virtuel et lance le jeu

# Couleurs pour l'affichage
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Récupérer le répertoire du script
SCRIPT_DIR="${0:a:h}"
cd "$SCRIPT_DIR"

echo "${BLUE}═══════════════════════════════════════${NC}"
echo "${BLUE}    Lancement de SunTzu Game${NC}"
echo "${BLUE}═══════════════════════════════════════${NC}"

# Vérifier si l'environnement virtuel existe
if [ ! -d "venv" ]; then
    echo "${RED}❌ Environnement virtuel non trouvé!${NC}"
    echo "${BLUE}Création de l'environnement virtuel...${NC}"
    python3 -m venv venv

    if [ $? -ne 0 ]; then
        echo "${RED}❌ Erreur lors de la création du venv${NC}"
        exit 1
    fi

    echo "${GREEN}✓ Environnement virtuel créé${NC}"

    # Activer l'environnement et installer les dépendances
    echo "${BLUE}Installation des dépendances...${NC}"
    source venv/bin/activate
    pip install -r requirements.txt

    if [ $? -ne 0 ]; then
        echo "${RED}❌ Erreur lors de l'installation des dépendances${NC}"
        deactivate
        exit 1
    fi

    echo "${GREEN}✓ Dépendances installées${NC}"
else
    # Activer l'environnement virtuel existant
    echo "${BLUE}Activation de l'environnement virtuel...${NC}"
    source venv/bin/activate
    echo "${GREEN}✓ Environnement virtuel activé${NC}"
fi

# Se déplacer dans le dossier du jeu
cd "SunTzuV01_BETA/"

# Lancer le jeu
echo "${GREEN}🎮 Lancement du jeu...${NC}"
echo "${BLUE}═══════════════════════════════════════${NC}\n"
python3 main.py

# Code de sortie du jeu
GAME_EXIT_CODE=$?

# Retourner au répertoire racine
cd ..

# Désactiver l'environnement virtuel
deactivate

echo "\n${BLUE}═══════════════════════════════════════${NC}"
if [ $GAME_EXIT_CODE -eq 0 ]; then
    echo "${GREEN}✓ Jeu terminé normalement${NC}"
else
    echo "${RED}❌ Le jeu s'est terminé avec une erreur (code: $GAME_EXIT_CODE)${NC}"
fi
echo "${BLUE}═══════════════════════════════════════${NC}"

exit $GAME_EXIT_CODE
