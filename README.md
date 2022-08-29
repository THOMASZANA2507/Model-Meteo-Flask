# Code source du projet "Déployer un modèle de prévision météo avec une API Flask" écrit pour HyperionDev.

Dans ce projet, nous prenons le modèle de regression logistique construit dans model.py qui prédit si dans une ville, il va pleuvoir ou non demain à partir des données comme humidité, vitesse du vent, direction du vent etc.. sous format json. En utilisant Flask pour créer une API, nous pouvons déployer ce modèle et créer une simple page Web pour charger les données des villes et prédire s'il va pleuvoir ou non demain.
Pour exécuter localement :

Installer pip et Python 3
Clonez ce référentiel git clone https://github.com/THOMASZANA2507/Model-Meteo-Flask.git
Accédez au répertoire de travail cd Model-Meteo-Flask
Installez les dépendances Python pip install -r requirements.txt
Exécutez l'API python serveur.py
Ouvrez un navigateur Web et accédez à http://localhost:5000

Pour exécuter à partir d'un lien heroku: https://deploymentprojetmeteo.herokuapp.com/
