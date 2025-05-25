# 마스킹을 사용한 Streamplot

이 단계에서는 마스킹을 사용하여 streamplot 을 생성합니다. 마스크를 생성하여 벡터 필드의 `U` 구성 요소에 적용합니다. 마스크된 영역은 streamline 에 의해 건너뛰어집니다.

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
