# マスク領域を区切る線の追加

最後に、マスク領域を区切る線を追加します。theta値の配列を作成し、`np.cos(theta)`と`np.sin(theta)`を使って半径`r0`の円を描画します。

```python
# Show the boundary between the regions:
theta = np.arange(0, np.pi / 2, 0.01)
plt.plot(r0 * np.cos(theta), r0 * np.sin(theta))
```
