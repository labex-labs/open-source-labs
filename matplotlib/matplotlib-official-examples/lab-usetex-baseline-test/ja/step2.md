# Matplotlib のフォントを設定する

Matplotlib のテキストに使用するフォントを設定する必要があります。Computer Modern フォントを使用し、Matplotlib の既定のフォントとして設定します。

```python
plt.rcParams.update({"mathtext.fontset": "cm", "mathtext.rm": "serif"})
```
