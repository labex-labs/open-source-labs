# 기본 플롯 생성

텍스트 요소를 사용하여 기본 플롯을 생성하는 것으로 시작해 보겠습니다. Python 스크립트에 다음 코드를 추가하십시오.

```python
import matplotlib.pyplot as plt

fig = plt.figure()
plt.axis([0, 10, 0, 10])
plt.text(5, 5, "Hello, Matplotlib!", ha='center')
plt.show()
```
