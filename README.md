<img src="data/images/quantmetry.png" width=400>

# Analyse des résultats du Grand Débat National

Courte expérimentation sur l'analyse des contributions du [Grand Débat National](https://granddebat.fr/).

Mots clés : NLP, TAL, LDA, Embeddings, TextRank

Auteurs : [Antoine SIMOULIN](https://github.com/AntoineSimoulin), [Antoine ISNARDY](https://github.com/antisrdy), [Thibaud REAL DEL SARTE](trealdelsarte@quantmetry.com)

**DISCLAIMER** : Quantmetry et les auteurs de ce notebook ne peuvent être tenus responsables de l'interprétation des réponses aux questions posées lors du Grand Débat. Le présent notebook fournit des outils d'analyse desdites réponses, non une interprétation.

# Objectifs

**Initier la mise à disposition, pour tout citoyen, de techniques d’Intelligence Artificielle destinées à appréhender le nombre important de contributions au Grand Débat :**
- Explorer les idées exprimées de manière récurrente
- Résumer les milliers de réponses à une question donnée en quelques extraits caractéristiques

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
