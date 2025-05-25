# 산점도 생성

선 그래프 외에도 Matplotlib 을 사용하면 산점도 (scatter plot) 를 생성할 수 있습니다. 산점도는 두 변수 간의 관계를 시각화하는 데 유용합니다.

```python
# Create the data
x = np.random.rand(50)
y = np.random.rand(50)

# Create the scatter plot
plt.scatter(x, y)

# Add title and axis labels
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()
```
