# Daten generieren

Als nächstes werden wir einen Gaussian-Mischungs-Datensatz mit zwei Komponenten generieren. Wir werden einen verschobenen Gaussian-Datensatz um (20, 20) zentrieren und einen nullzentrierten gedehnten Gaussian-Datensatz erstellen. Anschließend werden wir die beiden Datensätze zu dem endgültigen Trainingssatz zusammenfügen.

```python
n_samples = 300

# generiere zufällige Stichprobe, zwei Komponenten
np.random.seed(0)

# generiere sphärische Daten um (20, 20) zentriert
shifted_gaussian = np.random.randn(n_samples, 2) + np.array([20, 20])

# generiere nullzentrierte gedehnte Gaussian-Daten
C = np.array([[0.0, -0.7], [3.5, 0.7]])
stretched_gaussian = np.dot(np.random.randn(n_samples, 2), C)

# füge die beiden Datensätze zu dem endgültigen Trainingssatz zusammen
X_train = np.vstack([shifted_gaussian, stretched_gaussian])
```
