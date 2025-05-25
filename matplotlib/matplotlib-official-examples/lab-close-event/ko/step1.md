# Matplotlib 임포트 및 on_close 함수 정의

이 단계에서는 Matplotlib 을 임포트하고 figure 가 닫힐 때 호출될 `on_close` 함수를 정의합니다. 이 함수는 단순히 콘솔에 메시지를 출력합니다.

```python
import matplotlib.pyplot as plt

def on_close(event):
    print('Closed Figure!')
```
