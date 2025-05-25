# 산점도 (Scatter Plot) 생성

선 그래프 (line plot) 외에도 Matplotlib 은 산점도 (scatter plot) 도 생성할 수 있습니다. 다음은 예시입니다.

```python
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 500 * np.random.rand(50)

plt.scatter(x, y, c=colors, s=sizes)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot')
plt.show()
```
