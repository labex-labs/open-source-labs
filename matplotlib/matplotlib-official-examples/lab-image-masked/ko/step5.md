# 막대 그래프 생성

또 다른 일반적인 플롯 유형은 막대 그래프 (bar chart) 입니다. 막대 그래프는 서로 다른 범주의 값을 비교하는 데 유용합니다.

```python
# Create the data
x = ['A', 'B', 'C', 'D', 'E']
y = [3, 7, 1, 9, 4]

# Create the bar chart
plt.bar(x, y)

# Add title and axis labels
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')

plt.show()
```
