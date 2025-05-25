# 막대 그래프 만들기

이 단계에서는 Matplotlib 를 사용하여 막대 그래프 (bar chart) 를 만들 것입니다. 먼저 NumPy 의 `random()` 함수를 사용하여 플롯할 데이터를 생성합니다. 그런 다음 `bar()` 함수를 사용하여 플롯을 만듭니다.

```python
x = ['A', 'B', 'C', 'D', 'E']
y = np.random.randint(1, 10, 5)

plt.bar(x, y)
plt.show()
```
