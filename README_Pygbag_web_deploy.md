## 1. Comment lancer le jeu pour tester que tout est ok

### En local (Python standard)
```bash
python3 SunTzuV01_BETA/main.py
# ou via le script
sh launch_game_macOS.sh
```

### Pour le Web (Pygbag)
```bash
# Depuis la racine du projet
pygbag SunTzuV01_BETA
```
Accès via navigateur : `http://localhost:8000`

## 2. Comment déployer le jeu sur la github page

 - copier l'intégralité des fichiers du dossier :
```bash
./SunTzuV01_BETA/build/web 
```
 (générés par la commande pygbag précédente) 
 - dans le dossier :
```bash
./docs
```
 - commit et push sur la branch :
```bash
maxime/webGhPage/deployBranch
```
