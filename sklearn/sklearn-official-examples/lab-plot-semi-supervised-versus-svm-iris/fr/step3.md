# Configurer les classifieurs Self-training

Nous allons configurer deux classifieurs Self-training avec différents pourcentages de données étiquetées : 30 % et 50 %. Self-training est un algorithme d'apprentissage semi-supervisé qui entraîne un classifieur sur les données étiquetées puis l'utilise pour prédire les étiquettes des données non étiquetées. Les prédictions les plus sûres sont ajoutées aux données étiquetées et le processus est répété jusqu'à convergence.

```python
from sklearn.semi_supervised import SelfTrainingClassifier
from sklearn.svm import SVC

# Configurer les classifieurs Self-training
base_classifier = SVC(kernel="rbf", gamma=0.5, probability=True)
st30 = (
    SelfTrainingClassifier(base_classifier).fit(X, y_30),
    y_30,
    "Self-training 30% des données",
)
st50 = (
    SelfTrainingClassifier(base_classifier).fit(X, y_50),
    y_50,
    "Self-training 50% des données",
)
```
