# 선형 스케일 플롯 생성

우리가 탐구할 첫 번째 유형의 스케일 변환은 선형 (linear) 입니다. 이것은 Matplotlib 에서 사용되는 기본 스케일입니다. 선형 스케일 플롯을 생성하려면 `set_yscale()` 메서드를 사용하고 문자열 `'linear'`를 전달합니다. 또한 플롯에 제목과 그리드를 추가합니다.

```python
# linear
plt.plot(x, y)
plt.yscale('linear')
plt.title('Linear Scale')
plt.grid(True)
```
