# Labelpropagation

#### Überblick über den Labelpropagation-Algorithmus

Labelpropagation ist ein Typ von halbüberwachten Grapheninferenzalgorithmen. Es konstruiert einen Ähnlichkeitsgraphen über alle Elemente im Eingabedatensatz und verwendet diesen Graphen, um die Labels von den markierten Daten auf die unmarkierten Daten zu propagieren. Labelpropagation kann für Klassifizierungstasks verwendet werden und unterstützt Kernelmethoden, um die Daten in alternative Dimensionsräume zu projizieren.

#### Verwendung von Labelpropagation in scikit-learn

In scikit-learn sind zwei Labelpropagation-Modelle verfügbar: `LabelPropagation` und `LabelSpreading`. Beide Modelle konstruieren einen Ähnlichkeitsgraphen und propagieren die Labels. Hier ist ein Beispiel dafür, wie Labelpropagation verwendet werden kann:

```python
from sklearn.semi_supervised import LabelPropagation

# Erstellen eines Labelpropagation-Modells
label_propagation = LabelPropagation()

# Trainieren des Labelpropagation-Modells auf den markierten Daten
label_propagation.fit(X_labeled, y_labeled)

# Vorhersagen der Labels für neue Proben
y_pred = label_propagation.predict(X_test)
```

In obigem Beispiel sind `X_labeled` und `y_labeled` die markierten Daten, und `X_test` sind die neuen Proben, für die vorhergesagt werden soll.
