# 두 번째 서브플롯 생성

`rstride` 매개변수를 `0`으로, `cstride` 매개변수를 `10`으로 설정하여 두 번째 서브플롯을 생성합니다.

```python
ax2.plot_wireframe(X, Y, Z, rstride=0, cstride=10)
ax2.set_title("Row (y) stride set to 0")
```
