# SunTzu_game
thanks to SunTzu_Game_Board

**PRESS ESC TO EXIT**

**PRESS SPACE TO CONTINUE**

---

## Installation Rapide (Recommandée)

La méthode la plus simple pour lancer le jeu est d'utiliser les scripts de lancement automatiques.

### Prérequis

*   Python 3
*   Pip (le gestionnaire de paquets Python)

### Sur macOS/Linux

1.  Ouvrez un terminal à la racine du projet (`SunTzu_game`)

2. exécuter le fichier :
    ```bash
    sh ./launch_game_macOS.sh
    ```

Si besoin :

3.  Rendez le script exécutable (une seule fois) :
    ```bash
    chmod +x launch_game_macOS.sh
    ```

4.  Lancez le jeu :
    ```bash
    ./launch_game_macOS.sh
    ```

Le script s'occupe automatiquement de :
- Créer l'environnement virtuel si nécessaire
- Installer les dépendances
- Lancer le jeu
- Nettoyer à la fermeture

### Sur Windows

1.  Naviguez jusqu'au dossier du projet (`SunTzu_game`)

2.  Double-cliquez sur le fichier `launch_game_Windows.bat`

OU via l'invite de commandes :
```cmd
launch_game_Windows.bat
```

Le script s'occupe automatiquement de :
- Créer l'environnement virtuel si nécessaire
- Installer les dépendances
- Lancer le jeu
- Afficher les résultats

---

## Installation Manuelle (Avancée)

Si vous préférez gérer manuellement l'environnement virtuel, suivez ces étapes.

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
        ```cmd
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