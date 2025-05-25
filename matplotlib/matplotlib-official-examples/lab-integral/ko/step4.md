# 플롯 생성

`subplots`를 사용하여 figure 및 axis 객체를 생성합니다. `plot`을 사용하여 x 및 y 값을 플롯합니다. `set_ylim`을 사용하여 y 축의 한계를 0 에서 시작하도록 설정합니다.

```python
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ax.set_ylim(bottom=0)
```
