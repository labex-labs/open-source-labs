# Einrichten des Vektorisierers und Zurückhalten eines Testsets

```python
# Erzeuge den Vektorisierer und begrenze die Anzahl der Merkmale auf eine vernünftige
# Maximalzahl
vectorizer = HashingVectorizer(decode_error="ignore", n_features=2**18, alternate_sign=False)

# Iterator über die analysierten Reuters-SGML-Dateien.
data_stream = stream_reuters_documents()

# Wir lernen eine binäre Klassifikation zwischen der Klasse "acq" und allen anderen.
# "acq" wurde gewählt, da sie in den Reuters-Dateien mehr oder weniger gleichmäßig verteilt ist.
# Für andere Datensätze sollte man sich darum bemühen, ein Testset mit einem realistischen Anteil
# positiver Instanzen zu erstellen.
all_classes = np.array([0, 1])
positive_class = "acq"

# Hier sind einige Klassifizierer, die die `partial_fit`-Methode unterstützen
partial_fit_classifiers = {
    "SGD": SGDClassifier(max_iter=5),
    "Perceptron": Perceptron(),
    "NB Multinomial": MultinomialNB(alpha=0.01),
    "Passive-Aggressive": PassiveAggressiveClassifier(),
}

# Testdatenstatistiken
test_stats = {"n_test": 0, "n_test_pos": 0}

# Zunächst halten wir eine Anzahl von Beispielen zurück, um die Genauigkeit zu schätzen
n_test_documents = 1000
X_test_text, y_test = get_minibatch(data_stream, 1000)
X_test = vectorizer.transform(X_test_text)
test_stats["n_test"] += len(y_test)
test_stats["n_test_pos"] += sum(y_test)
print("Testset ist %d Dokumente (%d positiv)" % (len(y_test), sum(y_test)))
```
