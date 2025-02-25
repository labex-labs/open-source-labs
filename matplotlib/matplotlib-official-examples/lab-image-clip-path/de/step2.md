# Das Bild laden

Wir werden die `get_sample_data`-Methode aus `cbook` verwenden, um ein Beispielbild zu laden. Diese Methode gibt ein dateiliches Objekt zurück, das wir an `imshow` übergeben können, um das Bild anzuzeigen.

```python
with cbook.get_sample_data('grace_hopper.jpg') as image_file:
    image = plt.imread(image_file)
```
