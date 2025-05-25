# 주요 및 보조 눈금에 대한 자동 눈금 선택

```python
# Create data
t = np.arange(0.0, 100.0, 0.01)
s = np.sin(2 * np.pi * t) * np.exp(-t * 0.01)

# Plot the data
fig, ax = plt.subplots()
ax.plot(t, s)

# Set the minor locator
ax.xaxis.set_minor_locator(AutoMinorLocator())

# Set the tick parameters
ax.tick_params(which='both', width=2)
ax.tick_params(which='major', length=7)
ax.tick_params(which='minor', length=4, color='r')

# Display the plot
plt.show()
```

이 단계에서는 새로운 데이터를 생성하고 플롯합니다. 그런 다음 보조 눈금의 수를 자동으로 선택하도록 보조 로케이터 (minor locator) 를 설정합니다. 그 후, 주요 및 보조 눈금 모두에 대해 눈금 매개변수 (tick parameters), 즉 눈금의 너비, 길이 및 색상을 설정합니다. 마지막으로, 플롯을 표시합니다.
