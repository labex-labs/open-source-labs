# Bild laden

Als nächstes müssen wir das Bild laden, das wir auf das Diagramm legen möchten. Wir können die Methode `get_sample_data` aus dem Modul `matplotlib.cbook` verwenden, um ein Beispielbild zu laden. In diesem Beispiel verwenden wir das Bild `logo2.png`.

```python
with cbook.get_sample_data('logo2.png') as file:
    im = image.imread(file)
```
