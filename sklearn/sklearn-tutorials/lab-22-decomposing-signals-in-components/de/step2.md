# Unabhängige Komponentenanalyse (ICA)

#### ICA zur Trennung von Blindquellen

Die Unabhängige Komponentenanalyse (ICA) wird verwendet, um gemischte Signale in ihre ursprünglichen Quellenkomponenten zu trennen. Sie geht davon aus, dass die Komponenten statistisch unabhängig sind und durch einen linearen Entmischungsprozess extrahiert werden können. Die ICA kann mit der Klasse `FastICA` aus scikit-learn implementiert werden.

```python
from sklearn.decomposition import FastICA

# Erstellen eines ICA-Objekts mit n_components als Anzahl der gewünschten Komponenten
ica = FastICA(n_components=2)

# Anpassen des ICA-Modells an die gemischten Signale
ica.fit(mixed_signals)

# Trennen der gemischten Signale in die ursprünglichen Quellenkomponenten
source_components = ica.transform(mixed_signals)
```
