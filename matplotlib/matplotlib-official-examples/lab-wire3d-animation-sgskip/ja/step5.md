# プロットをアニメーション化する

5 番目のステップは、プロットをアニメーション化することです。phi の値の範囲を for ループで反復処理します。各反復では、前の線のコレクションを削除し、新しいデータを生成し、新しいワイヤーフレームを描画し、続ける前に短時間一時停止します。

```python
wframe = None
tstart = time.time()
for phi in np.linspace(0, 180. / np.pi, 100):
    if wframe:
        wframe.remove()
    Z = np.cos(2 * np.pi * X + phi) * (1 - np.hypot(X, Y))
    wframe = ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2)
    plt.pause(.001)
```
