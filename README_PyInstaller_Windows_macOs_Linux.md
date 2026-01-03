# Guide de Compilation avec PyInstaller (Windows / macOS / Linux)

Ce guide explique comment compiler le projet **SunTzu_game** en un exécutable autonome (.exe / .app / binaire) incluant toutes les ressources (images, sons).

## 1. Prérequis

Assurez-vous d'avoir installé **PyInstaller** dans votre environnement virtuel :

```bash
pip install pyinstaller
```

## 2. Préparation du Code (Indispensable)

Pour que l'exécutable unique (`--onefile`) trouve les images et les sons, il faut ajuster le dossier de travail au démarrage.

Ajoutez ces lignes **tout en haut** de votre fichier `SunTzuV01_BETA/main.py` (avant les autres imports ou juste après `import sys, os`) :

```python
import os
import sys

# Si le jeu est lancé en tant qu'exécutable (frozen), on se déplace dans le dossier temporaire d'extraction
if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)
```

*Sans cela, le jeu ne trouvera pas le dossier `ressources/` une fois compilé.*

## 3. Commandes de Compilation

Exécutez ces commandes depuis la **racine du projet** (le dossier contenant ce README et le dossier `SunTzuV01_BETA`).

### 🪟 Windows (PowerShell ou CMD)

**onefile:(plus propre)**
```powershell
pyinstaller --noconfirm --clean --onefile --windowed --name "SunTzuGame" --add-data "SunTzuV01_BETA/ressources;ressources" SunTzuV01_BETA/main.py
```

**onedir:(optimisé)**
```powershell
pyinstaller --noconfirm --clean --onedir --windowed --name "SunTzuGame" --add-data "SunTzuV01_BETA/ressources;ressources" SunTzuV01_BETA/main.py
```

*   **Résultat :** `dist/SunTzuGame.exe`
*   *Note : Le séparateur pour `--add-data` sous Windows est le point-virgule `;`.*

### 🍎 macOS (Terminal)

**onefile:(pas top)**
```bash
pyinstaller --noconfirm --clean --onefile --windowed --name "SunTzuGame" --add-data "SunTzuV01_BETA/ressources:ressources" SunTzuV01_BETA/main.py
```

**onedir:(optimisé)**
```bash
pyinstaller --noconfirm --clean --onedir --windowed --name "SunTzuGame" --add-data "SunTzuV01_BETA/ressources:ressources" SunTzuV01_BETA/main.py
```

*   **Résultat :** `dist/SunTzuGame.app`
*   *Note : Le séparateur pour `--add-data` sous macOS/Linux est deux-points `:`.*

### 🐧 Linux (Terminal)

**onefile:(plus propre)**
```bash
pyinstaller --noconfirm --clean --onefile --windowed --name "SunTzuGame" --add-data "SunTzuV01_BETA/ressources:ressources" SunTzuV01_BETA/main.py
```

**onedir:(optimisé)**
```bash
pyinstaller --noconfirm --clean --onedir --windowed --name "SunTzuGame" --add-data "SunTzuV01_BETA/ressources:ressources" SunTzuV01_BETA/main.py
```

*   **Résultat :** `dist/SunTzuGame` (binaire)

## 4. Détails des options

*   `--onefile` : Crée un seul fichier exécutable (plus facile à partager).
*   `--windowed` : Lance le jeu sans ouvrir de console (terminal) en arrière-plan.
*   `--add-data "SRC;DEST"` : Inclut le dossier `ressources` dans l'exécutable.
*   `--clean` : Nettoye les caches de compilation avant de construire.
*   `--name` : Nomme le fichier de sortie.

## 5. Résolution de problèmes

*   **Erreur "File not found" pour les images/sons :** Vérifiez que vous avez bien ajouté le bloc de code de l'étape 2 dans `main.py`.
*   **L'exécutable se ferme immédiatement :** Essayez de compiler **sans** l'option `--windowed` pour voir les erreurs s'afficher dans la console.
