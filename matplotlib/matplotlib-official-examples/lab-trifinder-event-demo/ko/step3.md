# 플롯 설정

이제 플롯을 설정할 수 있습니다. `plt.subplots()`를 사용하여 figure 와 axis 객체를 생성합니다. 그런 다음 `ax.triplot()`을 사용하여 triangulation 을 플롯합니다.

```python
fig, ax = plt.subplots()
ax.triplot(triang)
```
