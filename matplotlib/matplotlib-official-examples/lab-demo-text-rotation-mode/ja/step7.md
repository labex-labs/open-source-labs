# サブフィギュアを作成して `test_rotation_mode` 関数を呼び出す

2 つのサブフィギュアを作成し、`fig` と `mode` のパラメータを使って `test_rotation_mode` 関数を呼び出します。

```python
fig = plt.figure(figsize=(8, 5))
subfigs = fig.subfigures(1, 2)
test_rotation_mode(subfigs[0], "default")
test_rotation_mode(subfigs[1], "anchor")
plt.show()
```
