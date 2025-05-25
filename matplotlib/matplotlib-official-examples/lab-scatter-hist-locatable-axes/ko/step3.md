# 산점도 생성

이 단계에서는 2 단계에서 생성한 랜덤 데이터를 사용하여 산점도를 생성합니다.

```python
fig, ax = plt.subplots(figsize=(5.5, 5.5))
ax.scatter(x, y)
ax.set_aspect(1.)
```
