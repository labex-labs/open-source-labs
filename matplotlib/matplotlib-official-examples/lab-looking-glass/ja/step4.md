# データのプロット

手順 2 で生成したランダムなデータを、`plot()` 関数を使って 2 回プロットします。最初のプロットでは、透明度の値を 0.2 に設定し、2 番目のプロットでは、透明度の値を 1.0 に設定し、クリップパスを黄色い円形のパッチに設定します。

```python
ax.plot(x, y, alpha=0.2)
line, = ax.plot(x, y, alpha=1.0, clip_path=circ)
ax.set_title("Left click and drag to move looking glass")
```
