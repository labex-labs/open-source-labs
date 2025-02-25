# 目盛りラベルを非表示にする

各インセットから目盛りラベルを削除するには、`tick_params()` メソッドを使用して、`labelleft` と `labelbottom` を `False` に設定できます。

```python
# インセットの目盛りラベルを非表示にする
for axi in [axins, axins2, axins3, axins4]:
    axi.tick_params(labelleft=False, labelbottom=False)
```
