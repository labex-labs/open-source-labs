# FastICA-Algorithmus verwenden

In diesem Schritt verwenden wir den FastICA-Algorithmus, der Richtungen im Merkmalsraum findet, die mit Projektionen mit hoher Nicht-Gauß-Verteilung übereinstimmen.

```python
ica = FastICA(random_state=rng, whiten="arbitrary-variance")
S_ica_ = ica.fit(X).transform(X)  # Quellen schätzen

S_ica_ /= S_ica_.std(axis=0)
```
