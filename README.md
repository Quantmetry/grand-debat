<img src="data/images/quantmetry.png" width=400>

# Analyse des résultats du Grand Débat National

Courte participation à l'analyse des contributions du [Grand Débat National](https://granddebat.fr/).

Auteurs : [Antoine SIMOULIN](https://github.com/AntoineSimoulin), [Antoine ISNARDY](https://github.com/antisrdy), [Thibaud REAL DEL SARTE](trealdelsarte@quantmetry.com)

**DISCLAIMER** : Quantmetry et les auteurs de ce notebook ne peuvent être tenus responsables de l'interprétation des réponses aux questions posées lors du Grand Débat. Le présent notebook fournit une grille d'analyse desdites réponses, non une interprétation.

# Contexte

Le monde titrait le 22 février [Contributions au « grand débat » : comment analyser 68 millions de mots en deux semaines ?](https://www.lemonde.fr/politique/article/2019/02/21/contributions-au-grand-debat-comment-analyser-68-millions-de-mots-en-deux-semaines_5426369_823448.html). Chacun est libre d'y réfléchir puisque les données sont disponibles en "libre accès" sur le [site](https://www.data.gouv.fr/fr/datasets/donnees-ouvertes-du-grand-debat-national/#_) du grand débat. De plus, il est possible de proposer des contributions sous le format de notebooks depuis un git qui apparaissent sur le site.

# Objectifs

**Initier la mise à disposition, pour tout citoyen, de techniques d’Intelligence Artificielle destinées à appréhender le nombre important de contributions au Grand Débat :**
- Exploration de thèmes pour proposer une "synthèse" de l'immense masse de contributions proposées dans le cadre du grand débat via une procédure non supervisée de type LDA
- Résumé automatique des idées fortes via une procédure non supervisée de type Text Rank

Pour plus d'informations sur la démarche, se référer à cet [article](quantmetry.com/grand-debat)

# Utilisation

Il est conseillé de mener les expérimentations dans un environnement virtuel. Par exemple sous `conda`, lancer :

```bash
conda update conda
conda create --prefix .venv python=3.7
```

Il est ensuite nécessaire d'installer les dépendances du projets, listées dans le fichier `requirements.txt`.

Par suite, la démonstration figure dans le notebook `grand-debat.ipynb`, accessible en lançant depuis le répertoire source :

```bash
jupyter notebook
```
