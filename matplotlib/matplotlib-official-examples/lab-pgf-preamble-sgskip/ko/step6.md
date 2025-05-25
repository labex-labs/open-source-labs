# 막대 그래프 (Bar Plot) 생성

Matplotlib 은 막대 그래프 (bar plot) 도 생성할 수 있습니다. 다음은 예시입니다.

```python
x = ['A', 'B', 'C', 'D', 'E']
y = [3, 7, 1, 9, 4]

plt.bar(x, y)
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Plot')
plt.show()
```
