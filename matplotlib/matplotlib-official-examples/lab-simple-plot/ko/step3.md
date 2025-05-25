# 플롯 생성

이제 데이터를 갖추었으니 플롯을 생성할 수 있습니다. 먼저, `plt.subplots()`를 사용하여 figure 와 axis 객체를 생성합니다. 그런 다음, `ax.plot()`을 사용하여 데이터를 플롯합니다.

```python
fig, ax = plt.subplots()
ax.plot(t, s)
```
