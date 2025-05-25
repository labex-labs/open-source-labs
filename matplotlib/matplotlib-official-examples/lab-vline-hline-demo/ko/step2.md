# 데이터 정의

다음 단계는 플롯에 사용할 데이터를 정의하는 것입니다. NumPy 의 `arange` 함수를 사용하여 0 부터 5 까지 0.1 간격으로 값을 갖는 배열을 생성합니다. 이 배열을 x 축으로 사용합니다. 또한 NumPy 의 지수 함수와 사인 함수를 사용하여 y 축을 정의합니다.

```python
# Define the data
t = np.arange(0.0, 5.0, 0.1)
s = np.exp(-t) + np.sin(2 * np.pi * t) + 1
```
