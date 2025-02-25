# 軸スタイルの構成

次に、各軸の端に矢印を追加し、原点から X 軸と Y 軸を追加することで軸スタイルを構成します。

```python
for direction in ["xzero", "yzero"]:
    # 各軸の端に矢印を追加します
    ax.axis[direction].set_axisline_style("-|>")
    # 原点から X 軸と Y 軸を追加します
    ax.axis[direction].set_visible(True)

# 境界を非表示にします
for direction in ["left", "right", "bottom", "top"]:
    ax.axis[direction].set_visible(False)
```
