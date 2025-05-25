# 기본 매개변수를 설정하는 함수 생성

그림의 기본 매개변수를 설정하는 함수를 생성하려면 `rcParams.update()` 메서드를 사용할 수 있습니다. 이 메서드는 매개변수 이름과 값의 딕셔너리를 인수로 받아 현재 기본값을 새로운 값으로 업데이트합니다. 다음은 출판용 그림에 대한 몇 가지 기본 매개변수를 설정하는 함수의 예입니다.

```python
def set_pub():
    rcParams.update({
        "font.weight": "bold",  # bold fonts
        "tick.labelsize": 15,   # large tick labels
        "lines.linewidth": 1,   # thick lines
        "lines.color": "k",     # black lines
        "grid.color": "0.5",    # gray gridlines
        "grid.linestyle": "-",  # solid gridlines
        "grid.linewidth": 0.5,  # thin gridlines
        "savefig.dpi": 300,     # higher resolution output.
    })
```
