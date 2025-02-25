# マスキング付きの streamplot

このステップでは、マスキング付きの streamplot を作成します。マスクを作成し、ベクトルフィールドの `U` 成分に適用します。マスクされた領域は、流線によってスキップされます。

```python
mask = np.zeros(U.shape, dtype=bool)
mask[40:60, 40:60] = True
U[:20, :20] = np.nan
U = np.ma.array(U, mask=mask)

plt.streamplot(X, Y, U, V, color='r')
plt.title('Streamplot with Masking')
plt.imshow(~mask, extent=(-w, w, -w, w), alpha=0.5, cmap='gray', aspect='auto')
plt.gca().set_aspect('equal')
plt.show()
```
