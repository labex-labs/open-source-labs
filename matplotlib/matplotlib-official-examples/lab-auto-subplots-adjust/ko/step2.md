# 그래프 생성

몇 개의 긴 y-레이블이 있는 간단한 선 그래프를 만들어 보겠습니다.

```python
fig, ax = plt.subplots()
ax.plot(range(10))
ax.set_yticks([2, 5, 7], labels=['really, really, really', 'long', 'labels'])
```
