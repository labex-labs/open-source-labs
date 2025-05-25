# 메르카토르 투영 변환 스케일 플롯 생성

보너스로, 메르카토르 투영 (Mercator transform) 함수를 사용하여 플롯을 생성해 보겠습니다. 이는 Matplotlib 의 내장 함수는 아니지만, 자체 순방향 (forward) 및 역방향 (inverse) 함수를 정의하여 메르카토르 투영 스케일 플롯을 생성할 수 있습니다. 이 예제에서는 메르카토르 투영을 위한 `forward()` 및 `inverse()` 함수를 정의합니다. 또한 플롯에 제목과 그리드를 추가합니다.

```python
# Function Mercator transform
def forward(a):
    a = np.deg2rad(a)
    return np.rad2deg(np.log(np.abs(np.tan(a) + 1.0 / np.cos(a))))

def inverse(a):
    a = np.deg2rad(a)
    return np.rad2deg(np.arctan(np.sinh(a)))

t = np.arange(0, 170.0, 0.1)
s = t / 2.

plt.plot(t, s, '-', lw=2)
plt.yscale('function', functions=(forward, inverse))
plt.title('Mercator Transform Scale')
plt.grid(True)
plt.xlim([0, 180])
```
