# 눈금 형식 지정자 및 로케이터 설정

`set_major_formatter()` 메서드를 사용하여 5 단계에서 생성된 형식 지정 함수로 x 축 눈금 형식 지정자를 설정합니다. 또한 x 축 눈금 로케이터를 `MaxNLocator(integer=True)`로 설정하여 눈금 값이 정수 값을 갖도록 합니다.

```python
ax.xaxis.set_major_formatter(format_fn)
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
```
