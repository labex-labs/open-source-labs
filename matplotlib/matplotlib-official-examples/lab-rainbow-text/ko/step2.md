# 후속 텍스트 객체 생성

다음 단계는 `~.Axes.annotate`를 사용하여 후속 텍스트 객체를 생성하는 것입니다. 이 함수를 사용하면 이전 텍스트 객체에 상대적으로 텍스트 객체의 위치를 지정할 수 있습니다. 다음 코드는 이전 텍스트 객체의 오른쪽에 위치한 세 개의 텍스트 객체를 생성합니다.

```python
text = ax.annotate(
    " says,", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="gold", weight="bold")  # custom properties
text = ax.annotate(
    " hello", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="green", style="italic")  # custom properties
text = ax.annotate(
    " world!", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="blue", family="serif")  # custom properties
```
