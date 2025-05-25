# Formatter 사용

또한 formatter 를 사용하여 등고선 레이블을 서식 지정할 수 있습니다. 이를 통해 레이블을 특정 방식으로 서식 지정할 수 있습니다. 이 예제에서는 `LogFormatterMathtext`를 사용하여 레이블을 서식 지정합니다.

```python
fig2, ax2 = plt.subplots()
CS2 = ax2.contour(X, Y, 100**Z, locator=plt.LogLocator())
fmt = ticker.LogFormatterMathtext()
fmt.create_dummy_axis()
ax2.clabel(CS2, CS2.levels, fmt=fmt)
ax2.set_title("$100^Z$")

plt.show()
```
