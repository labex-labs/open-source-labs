# 데이터 플롯

이 단계에서는 이전 단계에서 생성한 샘플 데이터를 플롯합니다. `for` 루프를 사용하여 서로 다른 위상을 가진 여러 사인파를 플롯합니다.

```python
fig, ax = plt.subplots()

ncolors = len(plt.rcParams['axes.prop_cycle'])
shift = np.linspace(0, L, ncolors, endpoint=False)

for s in shift:
    # Plot the sine wave with a phase shift of s
    ax.plot(x, np.sin(x + s), 'o-')

ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_title("'dark_background' style sheet")

plt.show()
```
