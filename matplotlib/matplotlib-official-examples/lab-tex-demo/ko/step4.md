# 산점도 만들기

이 단계에서는 Matplotlib 를 사용하여 산점도 (scatter plot) 를 만들 것입니다. 먼저 NumPy 의 `random()` 함수를 사용하여 플롯할 임의의 데이터를 생성합니다. 그런 다음 `scatter()` 함수를 사용하여 플롯을 만듭니다.

```python
x = np.random.randn(100)
y = np.random.randn(100)

plt.scatter(x, y)
plt.show()
```
