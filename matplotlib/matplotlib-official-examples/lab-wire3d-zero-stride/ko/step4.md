# 첫 번째 서브플롯 생성

`rstride` 매개변수를 `10`으로, `cstride` 매개변수를 `0`으로 설정하여 첫 번째 서브플롯을 생성합니다.

```python
ax1.plot_wireframe(X, Y, Z, rstride=10, cstride=0)
ax1.set_title("Column (x) stride set to 0")
```
