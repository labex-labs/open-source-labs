# 그림 및 축 설정

`fig.add_axes` 메서드를 사용하여 그림 객체를 생성하고 네 개의 축 객체를 설정합니다.

```python
fig = plt.figure(figsize=(5.5, 4))
rect = (0.1, 0.1, 0.8, 0.8)
ax = [fig.add_axes(rect, label="%d" % i) for i in range(4)]
```
