# Matplotlibのフォントを設定する

Matplotlibのテキストに使用するフォントを設定する必要があります。Computer Modernフォントを使用し、Matplotlibの既定のフォントとして設定します。

```python
plt.rcParams.update({"mathtext.fontset": "cm", "mathtext.rm": "serif"})
```
