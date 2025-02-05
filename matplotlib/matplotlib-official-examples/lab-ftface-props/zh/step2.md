# 加载字体

在这一步中，我们将加载要使用的字体。我们将使用 Matplotlib 附带的一种字体。

```python
font = ft.FT2Font(
    os.path.join(matplotlib.get_data_path(),
                 'fonts/ttf/DejaVuSans-Oblique.ttf'))
```
