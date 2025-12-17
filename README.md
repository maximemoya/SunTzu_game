# SunTzu_game
SunTzu_Game

PRESS ESC TO EXIT
PRESS SPACE TO CONTINUE

## Comment exécuter le jeu (Méthode Recommandée)

Ce projet est une application graphique développée en Python. Il est recommandé d'utiliser un environnement virtuel (`venv`) pour isoler les dépendances du projet.

### Prérequis

*   Python 3
*   Pip (le gestionnaire de paquets Python)

### Installation

1.  **Créez un environnement virtuel :**
    Ouvrez un terminal à la racine du projet (`SunTzu_game`) et exécutez :
    ```bash
    python3 -m venv venv
    ```

2.  **Activez l'environnement virtuel :**
    *   **Sur macOS/Linux :**
        ```bash
        source venv/bin/activate
        ```
    *   **Sur Windows :**
        ```bash
        venv\Scripts\activate
        ```
    *(Votre terminal devrait maintenant afficher `(venv)` au début de la ligne.)*

3.  **Installez les dépendances :**
    Avec l'environnement activé, installez les bibliothèques requises à partir du fichier `requirements.txt` :
    ```bash
    pip install -r requirements.txt
    ```

### Exécution

1.  Assurez-vous que l'environnement virtuel est toujours activé.

2.  Déplacez-vous dans le sous-dossier de l'application :
    ```bash
    cd "SumTsu V01_BETA/"
    ```

3.  Lancez le jeu :
    ```bash
    python3 main.py
    ```

### Quitter l'environnement virtuel

Lorsque vous avez fini de travailler sur le projet, vous pouvez désactiver l'environnement avec la commande :
```bash
deactivate
```