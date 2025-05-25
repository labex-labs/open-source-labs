# 사용자 정의 스케일 플롯 생성

마지막으로 탐구할 스케일 변환 유형은 사용자 정의 (custom) 입니다. 이를 통해 스케일 변환을 위한 자체 순방향 (forward) 및 역방향 (inverse) 함수를 정의할 수 있습니다. 이 예제에서는 데이터의 제곱근을 취하는 사용자 정의 함수를 정의합니다. 사용자 정의 스케일 플롯을 생성하려면 `set_yscale()` 메서드를 사용하고 문자열 `'function'`을 전달합니다. 또한 `forward()` 및 `inverse()` 함수를 정의하고 이를 `functions` 매개변수에 인수로 전달합니다. 또한 플롯에 제목과 그리드를 추가합니다.

```python
# Function x**(1/2)
def forward(x):
    return x**(1/2)

def inverse(x):
    return x**2

plt.plot(x, y)
plt.yscale('function', functions=(forward, inverse))
plt.title('Custom Scale')
plt.grid(True)
```
