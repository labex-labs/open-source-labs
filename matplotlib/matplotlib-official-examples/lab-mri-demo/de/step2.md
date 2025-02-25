# Laden der MRI-Bilddaten

Wir werden die `get_sample_data`-Funktion aus `matplotlib` verwenden, um das Beispiel-MRI-Bild zu laden. Das Bild ist im 256x256 16-Bit-Ganzzahlformat.

```python
with cbook.get_sample_data('s1045.ima.gz') as dfile:
    im = np.frombuffer(dfile.read(), np.uint16).reshape((256, 256))
```
