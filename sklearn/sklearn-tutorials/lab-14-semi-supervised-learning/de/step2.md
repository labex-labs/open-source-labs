# Selbsttraining

#### Überblick über den Selbsttraining-Algorithmus

Der Selbsttraining-Algorithmus basiert auf Yarowskys Algorithmus. Er ermöglicht es einem überwachten Klassifikator, als halbüberwachter Klassifikator zu funktionieren, indem er sich anhand von unmarkierten Daten lernt. Der Algorithmus funktioniert, indem er den überwachten Klassifikator iterativ auf den markierten und unmarkierten Daten trainiert und dann die Vorhersagen für die unmarkierten Daten verwendet, um einen Teilmengen dieser Proben der markierten Daten hinzuzufügen. Der Algorithmus iteriert fort, bis alle Proben Labels haben oder keine neuen Proben in einer Iteration ausgewählt werden.

#### Verwendung von Selbsttraining in scikit-learn

In scikit-learn wird der Selbsttraining-Algorithmus in der Klasse `SelfTrainingClassifier` implementiert. Um diesen Algorithmus zu verwenden, müssen Sie einen überwachten Klassifikator angeben, der die `predict_proba`-Methode implementiert. Hier ist ein Beispiel dafür, wie der Selbsttraining-Algorithmus verwendet werden kann:

```python
from sklearn.semi_supervised import SelfTrainingClassifier
from sklearn.linear_model import LogisticRegression

# Erstellen eines logistischen Regressionsklassifikators
classifier = LogisticRegression()

# Erstellen eines Selbsttraining-Klassifikators mit dem logistischen Regressionsklassifikator als Basisklassifikator
self_training_classifier = SelfTrainingClassifier(classifier)

# Trainieren des Selbsttraining-Klassifikators auf den markierten und unmarkierten Daten
self_training_classifier.fit(X_labeled, y_labeled, X_unlabeled)

# Vorhersagen der Labels für neue Proben
y_pred = self_training_classifier.predict(X_test)
```

In obigem Beispiel sind `X_labeled` und `y_labeled` die markierten Daten, `X_unlabeled` die unmarkierten Daten und `X_test` die neuen Proben, für die vorhergesagt werden soll.
