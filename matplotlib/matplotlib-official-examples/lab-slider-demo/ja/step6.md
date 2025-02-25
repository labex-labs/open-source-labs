# スライダーに更新関数を登録する

次に、更新関数を各スライダーに登録して、スライダーを調整するたびにその関数が呼び出されるようにします。

```python
freq_slider.on_changed(update)
amp_slider.on_changed(update)
```
