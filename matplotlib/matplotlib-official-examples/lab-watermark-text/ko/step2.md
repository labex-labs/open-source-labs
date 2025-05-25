# 데이터 생성

플롯할 임의의 데이터를 생성해 보겠습니다.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

fig, ax = plt.subplots()
ax.plot(np.random.rand(20), '-o', ms=20, lw=2, alpha=0.7, mfc='orange')
ax.grid()
```
