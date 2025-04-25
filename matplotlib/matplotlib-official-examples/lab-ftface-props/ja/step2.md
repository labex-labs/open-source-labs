# フォントを読み込む

このステップでは、使用するフォントを読み込みます。Matplotlib に同梱されているフォントを使用します。

```python
font = ft.FT2Font(
    os.path.join(matplotlib.get_data_path(),
                 'fonts/ttf/DejaVuSans-Oblique.ttf'))
```
