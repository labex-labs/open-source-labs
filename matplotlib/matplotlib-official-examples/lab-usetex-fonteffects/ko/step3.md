# 폰트 함수 정의

이 단계에서는 폰트를 설정하는 함수를 정의합니다. 이 함수는 폰트 이름을 인수로 받아 지정된 이름으로 폰트를 설정하는 문자열을 반환합니다.

```python
def setfont(font):
    return rf'\font\a {font} at 14pt\a '
```
