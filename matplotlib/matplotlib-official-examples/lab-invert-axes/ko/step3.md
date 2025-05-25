# 플롯 생성

이제 Matplotlib 를 사용하여 플롯을 생성할 수 있습니다. `plot` 함수를 사용하여 데이터를 플롯하고, `set_xlim` 함수를 사용하여 x 축의 범위를 설정합니다.

```python
fig, ax = plt.subplots()

ax.plot(t, s)
ax.set_xlim(5, 0)  # decreasing time
ax.set_xlabel('decreasing time (s)')
ax.set_ylabel('voltage (mV)')
ax.set_title('Should be growing...')
ax.grid(True)

plt.show()
```
