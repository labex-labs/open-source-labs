# 마스크된 풍향 막대 그래프 생성

마스크된 배열을 사용하여 마스크된 풍향 막대 그래프를 생성할 수도 있습니다. 이 경우, 하나의 벡터 값을 잘못된 값으로 변경하고 마스크합니다.

```python
masked_u = np.ma.masked_array(U)
masked_u[4] = 1000  # Bad value that should not be plotted when masked
masked_u[4] = np.ma.masked

plt.barbs(X, Y, masked_u, V, length=8, pivot='middle')
plt.show()
```
