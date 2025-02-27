# Entraînement

Dans cette étape, nous entraînons le modèle de pipeline défini dans l'étape précédente. Nous définissons les hyperparamètres du modèle (taux d'apprentissage, taille de la couche cachée, régularisation), puis ajustons les données d'entraînement au modèle.

```python
from sklearn.base import clone

# Hyper-paramètres. Ces paramètres ont été définis par validation croisée,
# en utilisant GridSearchCV. Ici, nous ne réalisons pas de validation croisée pour
# gagner du temps.
rbm.learning_rate = 0.06
rbm.n_iter = 10

# Plus de composants tendent à donner une meilleure performance de prédiction, mais une
# durée d'ajustement plus longue
rbm.n_components = 100
logistic.C = 6000

# Entraînement du pipeline RBM-Logistique
rbm_features_classifier.fit(X_train, Y_train)
```
