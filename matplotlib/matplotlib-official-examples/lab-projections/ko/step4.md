# 데이터 플롯

`plot_wireframe`을 사용하여 세 개의 서브플롯 각각에 데이터를 플롯합니다.

```python
for ax in axs:
    ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
```
