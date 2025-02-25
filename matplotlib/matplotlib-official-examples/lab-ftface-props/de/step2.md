# Lade Schriftart

In diesem Schritt laden wir die Schriftart, mit der wir arbeiten werden. Wir werden eine Schriftart verwenden, die mit Matplotlib mitgeliefert wird.

```python
font = ft.FT2Font(
    os.path.join(matplotlib.get_data_path(),
                 'fonts/ttf/DejaVuSans-Oblique.ttf'))
```
