<div align="center">

# 🏯 SunTzu_game

*"L'art de la guerre, c'est de soumettre l'ennemi sans combat."*

[![Tester le jeu](https://img.shields.io/badge/Pour_tester_le_jeu_:-CLIQUEZ_ICI-orange?labelColor=blue&style=for-the-badge&logo=joycon)](https://maximemoya.github.io/SunTzu_game/)

**Note :** Version Web. Prévoir **30 à 60 secondes** de chargement selon votre connexion.

---
</div>

<div align="center">
  <kbd>
    <img src="https://github.com/user-attachments/assets/000f12ff-7f8d-4898-b5fe-80514b184a6a" alt="Game Demo" width="800" style="border-radius: 10px;">
  </kbd>
</div>

<br />

<div align="center">
  <h3>🎮 Aperçu du Gameplay</h3>
</div>

<table align="center">
  <tr>
    <td align="center" width="33%">
      <img src="https://github.com/user-attachments/assets/d2ce3d01-0b20-4d1e-9194-f4298dc4afe9" alt="Blue Team" style="border-radius: 10px;"><br />
      <sub><b>Blue Team Selection</b></sub>
    </td>
    <td align="center" width="33%">
      <img src="https://github.com/user-attachments/assets/230a2f8a-b447-497b-87a0-0a0d2f21d794" alt="Red Team" style="border-radius: 10px;"><br />
      <sub><b>Red Team Selection</b></sub>
    </td>
    <td align="center" width="33%">
      <img src="https://github.com/user-attachments/assets/1e1822e3-a77c-42ff-968e-dc79e462a204" alt="Battleground" style="border-radius: 10px;"><br />
      <sub><b>Battleground Area</b></sub>
    </td>
  </tr>
</table>

<br />

---

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Pygame-active?style=for-the-badge&logo=python&logoColor=white&color=yellow" />
</p>

## 1 - Installation Rapide (Recommandée)

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

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=auto&height=100&section=footer" width="100%"/>
</p>
<br></br>

## 2 - Installation Manuelle (Avancée)

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

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=auto&height=100&section=footer" width="100%"/>
</p>

## 3 - Commandes en jeu

- **ECHAP POUR QUITTER LA PARTIE**

- **ESPACE POUR CONTINUER**

- **DRAG AND DROP POUR BOUGER LES CARTES**

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=auto&height=100&section=footer" width="100%"/>
</p>

## 4 - 🤝 Contribuer — Génération des binaires (PyInstaller)

Les contributeurs peuvent aider à la diffusion du jeu en **générant les versions natives** pour les plateformes qu'ils utilisent :
*   🪟 **Windows** → `.exe`
*   🐧 **Linux** → binaire exécutable

Le projet utilise **PyInstaller** pour packager le jeu Python + Pygame en une application autonome.

---

### 📦 Pré-requis

1.  **Python 3.x** installé.
2.  **Pip** à jour.
3.  Le projet cloné localement.
4.  Installer les dépendances du projet : `pip install -r requirements.txt`.
5.  Installer PyInstaller :
    ```bash
    pip install pyinstaller
    ```

---

### 🪟 Windows (PowerShell ou CMD)

> [!IMPORTANT]
> Le build doit impérativement être effectué sur un système **Windows**.

#### ✅ Mode `onefile` (Recommandé pour le partage simple)
*Génère un seul fichier .exe facile à distribuer.*
```powershell
pyinstaller --noconfirm --clean --onefile --windowed `
  --name "SunTzuGame" `
  --add-data "SunTzuV01_BETA/ressources;ressources" `
  SunTzuV01_BETA/main.py
```

#### ✅ Mode `onedir` (Optimisé pour la performance)
*Lancement instantané, mais nécessite de zipper le dossier `dist/SunTzuGame` complet.*
```powershell
pyinstaller --noconfirm --clean --onedir --windowed `
  --name "SunTzuGame" `
  --add-data "SunTzuV01_BETA/ressources;ressources" `
  SunTzuV01_BETA/main.py
```

**Résultats :**
*   `dist/SunTzuGame.exe` (onefile)
*   `dist/SunTzuGame/SunTzuGame.exe` (onedir)

> [!NOTE]
> Sous Windows, le séparateur pour `--add-data` est le point-virgule ( `;` ).

---

### 🐧 Linux (Terminal)

> [!IMPORTANT]
> Le build doit impérativement être effectué sur un système **Linux**.

#### ✅ Mode `onefile` (Binaire unique)
```bash
pyinstaller --noconfirm --clean --onefile --windowed \
  --name "SunTzuGame" \
  --add-data "SunTzuV01_BETA/ressources:ressources" \
  SunTzuV01_BETA/main.py
```

#### ✅ Mode `onedir` (Optimisé)
```bash
pyinstaller --noconfirm --clean --onedir --windowed \
  --name "SunTzuGame" \
  --add-data "SunTzuV01_BETA/ressources:ressources" \
  SunTzuV01_BETA/main.py
```

**Résultats :**
*   `dist/SunTzuGame` (binaire unique)
*   `dist/SunTzuGame/SunTzuGame` (binaire dans dossier)

> [!NOTE]
> Sous Linux, le séparateur pour `--add-data` est le deux-points ( `:` ).

---

### 🧪 Tests recommandés avant Soumission (PR)

Avant de proposer un binaire ou une modification du processus de build, merci de vérifier sur une machine test :
- [ ] **Lancement :** Le jeu démarre-t-il sans terminal en arrière-plan ?
- [ ] **Assets :** Les images s'affichent-elles correctement ?
- [ ] **Audio :** Les musiques et sons se lancent-ils ?
- [ ] **EventHandlers :** Les clics et drag&drop fonctionnent-ils ?
- [ ] **Stabilité :** Le jeu se ferme-t-il proprement avec `ESC` ?

---

**Merci pour votre aide !** 🙏
Chaque contribution rapproche **SunTzu_game** d’une diffusion multiplateforme. ⚔️🏯

<br></br>

<p align="center">
  Réalisé avec ❤️ par <b>Maxime Moya</b> — <i>Développeur Passionné</i>
  <br>
</p>
<br></br>
<br></br>
<br></br>

