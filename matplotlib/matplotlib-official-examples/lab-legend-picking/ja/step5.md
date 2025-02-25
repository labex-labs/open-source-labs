# 凡例の線を元の線にマッピングする

辞書を使って凡例の線を元の線にマッピングします。

```python
lines = [line1, line2]
lined = {}  # 凡例の線を元の線にマッピングします。
for legline, origline in zip(leg.get_lines(), lines):
    legline.set_picker(True)  # 凡例の線でのピッキングを有効にします。
    lined[legline] = origline
```
