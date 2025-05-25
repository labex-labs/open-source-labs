# 서브플롯 사용자 정의

필요에 따라 서브플롯을 사용자 정의할 수 있습니다. 예를 들어, `fig.suptitle()` 함수를 사용하여 그림의 제목을 설정하고, `format_axes()` 함수를 사용하여 축의 형식을 지정할 수 있습니다.

```python
fig.suptitle("GridSpec")

def format_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)

format_axes(fig)
```
