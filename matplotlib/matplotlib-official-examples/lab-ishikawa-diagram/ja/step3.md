# 魚骨図を作成する

ここでは、魚骨図を作成します。まず、グラフと軸のオブジェクトを作成します。

```python
fig, ax = plt.subplots(figsize=(10, 6), layout='constrained')
```

次に、軸の x と y の範囲を設定し、軸を非表示にします。

```python
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.axis('off')
```
