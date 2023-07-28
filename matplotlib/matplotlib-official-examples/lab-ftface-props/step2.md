# Load Font

In this step, we will load the font that we will be working with. We will use a font shipped with Matplotlib.

```python
font = ft.FT2Font(
    os.path.join(matplotlib.get_data_path(),
                 'fonts/ttf/DejaVuSans-Oblique.ttf'))
```
