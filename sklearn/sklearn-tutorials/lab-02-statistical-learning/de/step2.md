# Das Umformen von Daten

Manchmal kann die Dateninitialisierung nicht die von scikit-learn erforderliche Form haben. In solchen Fällen müssen wir die Daten vorverarbeiten, um sie in die Form `(n_samples, n_features)` zu transformieren. Ein Beispiel für das Umformen von Daten ist der Digits-Datensatz, der aus 1797 8x8-Bildern von handschriftlichen Ziffern besteht:

```python
digits = datasets.load_digits()
print(digits.images.shape)
```

Ausgabe:

```
(1797, 8, 8)
```

Um diesen Datensatz mit scikit-learn zu verwenden, müssen wir jedes 8x8-Bild in einen Merkmalsvektor der Länge 64 umformen:

```python
data = digits.images.reshape((digits.images.shape[0], -1))
```
