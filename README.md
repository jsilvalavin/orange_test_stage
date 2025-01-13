# README
Le présent dépôt contient les fichiers nécessaires pour l'étude et la prediction de la vente des modèles de téléphone démandés. Le dépôt contient les fichiers suivants:

- Dossier data
    - 'telecom_sales_data.csv': données de vente des modèles de téléphone avec les variables suivantes, indexées par la date, entre 2019-01-01 et 2024-12-31:
        - 'competition_index': indice de la concurrence
        - 'costumer_satisfaction': satisfaction du client
        - 'purchasing_power_index': indice de pouvoir d'achat
        - 'weather_condition': condition météorologique
        - 'tech_event': événement technologique
        - '5g_phase': phase 5G
        - ' store_traffic': trafic en magasin
        - 'public_transport': transport public
        - 'city': ville
        - 'jPhone_Pro_revenue': revenu de jPhone Pro
        - 'Kaggle_Pixel_revenue': revenu de Kaggle Pixel
        - 'Planet_SX_revenue': revenu de Planet SX
- Dossier notebooks
    - 'exploration.ipynb': notebook contenant l'exploration statistique des données et les _insights_ obtenus à partir de cette exploration
    - 'modeling.ipynb': notebook contenant la modélisation des données et l'exploration des modèles de prédiction et son performance dans les données d'apprendissage
- Dossier presentation
    - 'rapport.pdf': présentation des résultats obtenus
- Dossier src
    - 'data_processing.py': script contenant les fonctions de traitement des données, comme la transformation des variables catégorielles en variables numériques.
    - 'feature_engineering.py': script contenant les fonctions de création de nouvelles variables à partir des variables existantes, spécialement les variables temporelles.
    - 'modeling.py': script contenant les fonctions de modélisation des données, la prediction des variables predicteurs et la prediciton des variables cibles.
    - '__main__.py': script principal pour lancer le traitement des données, la création des nouvelles variables, la modélisation des données et la prédiction des variables cibles.
- Dossier predictions
    - 'predictions_ville.csv': fichier contenant les prédictions des variables cibles pour la ville choisie.

Est important de mentioner que le code est ecrit en anglais, car est très plus congruent avec les fonctions de Python et les librairies utilisées et est plus facile pour moi encore, car je connais mieux la terminologie en anglais. Cependant, le README et le rapport sont en français pour faciliter la compréhension des résultats obtenus.

# Installation
Est necessaire d'avoir Python 3.4, jupyter notebook et les librairies suivantes pour lancer le code:
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- xgboost
- statsmodels
- os
La éxecution du code peut être, plus facilement réalisée dans google colab.

# Utilisation	
Pour l'exploration et la modélisation des données, il suffit d'ouvrir les notebooks 'exploration.ipynb' et 'modeling.ipynb' dans un environnement de jupyter notebook et d'exécuter les cellules du notebook. Est important d'éxecuter les cellules dans l'ordre pour éviter des erreurs. 

Pour lancer le traitement des données, la création des nouvelles variables, la modélisation des données et la prédiction des variables cibles, il suffit d'exécuter le script '__main__.py' dans un terminal. Ce fichier donnera l'election de la ville pour laquelle on veut faire la prédiction des variables cibles. Les prédictions des variables cibles,  sont stockées dans le dossier 'predictions' sous le nom 'predictions_ville.csv' et les données prédits sont montrés dans un graphique.