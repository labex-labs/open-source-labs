# Generieren der Histogrammdaten

Jetzt, wo wir unsere zufälligen Daten haben, können wir mit numpy ein Histogramm generieren. Wir werden 50 Bins verwenden, um unser Histogramm zu erstellen. Fügen Sie den folgenden Code hinzu:

```python
n, bins = np.histogram(data, 50)
```
