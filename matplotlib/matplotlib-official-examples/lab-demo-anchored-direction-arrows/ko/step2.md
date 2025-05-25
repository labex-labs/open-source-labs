# 플롯 생성

다음으로, NumPy 를 사용하여 간단한 플롯을 생성합니다. 이 플롯은 앵커된 방향 화살표의 배경 역할을 합니다.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

fig, ax = plt.subplots()
ax.imshow(np.random.random((10, 10)))
```
