# Prédiction des ventes et budgets publicitaires

## Français

Ce projet explore la relation entre les dépenses publicitaires à la télévision (`tv`), à la radio (`radio`) et dans les journaux (`journaux`), et les ventes (`ventes`). Le script [`main.py`](main.py) charge le jeu de données [`data/advertising.csv`](data/advertising.csv), examine les données, puis entraîne et évalue des modèles de régression linéaire.

### Ce que fait le script

- Affiche un aperçu et des statistiques descriptives des données.
- Prépare des graphiques bivariés avec une droite de régression pour chaque canal publicitaire.
- Entraîne une régression linéaire avec les trois canaux comme variables prédictives.
- Sépare les données en ensembles d’entraînement et de test (80 % / 20 %), avec `random_state=42` pour rendre cette séparation reproductible.
- Évalue le modèle à l’aide de la MAPE et d’une erreur quadratique.
- Ajoute un terme quadratique `tv2 = tv ** 2`, normalise les colonnes entre 0 et 1, puis entraîne et évalue un second modèle.

### Notions principales

La régression linéaire est un modèle simple pour prédire une valeur continue à partir de variables prédictives. Elle convient lorsque la relation entre la cible et les prédicteurs est suffisamment linéaire. Si cette relation est courbe, ajouter des termes polynomiaux — par exemple un terme quadratique — peut aider le modèle à la représenter.

La séparation avec `train_test_split` permet d’évaluer le modèle sur des données non utilisées pour son entraînement. Fixer `random_state` rend cette séparation reproductible. La normalisation met les variables sur une échelle comparable et facilite l’interprétation relative des coefficients, mais ceux-ci doivent être interprétés en tenant compte de cette mise à l’échelle. Dans le script actuel, le scaler est ajusté avant la séparation entraînement/test; pour une évaluation plus rigoureuse, il faudrait l’ajuster uniquement sur les données d’entraînement.

La RMSE (racine de l’erreur quadratique moyenne) et la MAPE (erreur absolue moyenne en pourcentage) sont des métriques d’évaluation. **À noter :** le script affiche actuellement `mean_squared_error` avec l’étiquette `RMSE`; cette fonction renvoie le MSE, pas sa racine. Pour afficher la RMSE, il faut prendre la racine carrée du résultat.

### Exécution

Depuis la racine du projet, installez les dépendances si nécessaire, puis lancez :

```bash
python main.py
```

Dépendances utilisées : `pandas`, `numpy`, `seaborn`, `matplotlib` et `scikit-learn`.

Les appels à `plt.show()` sont commentés dans le script : décommentez-les si vous souhaitez afficher les graphiques.

## English

This project explores the relationship between advertising spend on TV (`tv`), radio (`radio`), and newspapers (`journaux`), and sales (`ventes`). The [`main.py`](main.py) script loads [`data/advertising.csv`](data/advertising.csv), inspects the data, and trains and evaluates linear regression models.

### What the script does

- Prints a data preview and descriptive statistics.
- Prepares bivariate plots with a regression line for each advertising channel.
- Trains a linear regression model using the three channels as predictors.
- Splits the data into training and test sets (80% / 20%), using `random_state=42` to make the split reproducible.
- Evaluates the model using MAPE and a squared-error metric.
- Adds a quadratic term, `tv2 = tv ** 2`, scales the columns to the 0–1 range, and trains and evaluates a second model.

### Key concepts

Linear regression is a simple model for predicting a continuous value from predictor variables. It is appropriate when the relationship between the target and predictors is sufficiently linear. If that relationship is curved, adding polynomial terms — such as a quadratic term — can help the model capture it.

`train_test_split` makes it possible to evaluate a model on data that was not used for training. Setting `random_state` makes the split reproducible. Scaling puts variables on comparable ranges and helps with relative coefficient interpretation, though coefficients must be understood in the context of that scaling. In the current script, the scaler is fitted before the train/test split; for a more rigorous evaluation, it should be fitted on the training data only.

RMSE (root mean squared error) and MAPE (mean absolute percentage error) are evaluation metrics. **Note:** the script currently prints `mean_squared_error` with the label `RMSE`; that function returns MSE, not its square root. To report RMSE, take the square root of the result.

### Running the project

From the project root, install the dependencies if needed, then run:

```bash
python main.py
```

Dependencies used: `pandas`, `numpy`, `seaborn`, `matplotlib`, and `scikit-learn`.

The `plt.show()` calls are commented out in the script; uncomment them to display the plots.
