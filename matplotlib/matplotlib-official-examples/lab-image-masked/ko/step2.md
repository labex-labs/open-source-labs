# 데이터 생성

다음으로, 플롯에 사용할 데이터를 생성합니다. 이 튜토리얼에서는 간단한 선 그래프를 생성합니다.

```python
# Create the data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot the data
plt.plot(x, y)
plt.show()
```
