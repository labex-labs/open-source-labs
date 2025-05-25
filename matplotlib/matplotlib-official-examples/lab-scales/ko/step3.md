# 로그 스케일 플롯 생성

다음으로 탐구할 스케일 변환 유형은 로그 (logarithmic) 입니다. 로그 스케일 플롯을 생성하려면 `set_yscale()` 메서드를 사용하고 문자열 `'log'`를 전달합니다. 또한 플롯에 제목과 그리드를 추가합니다.

```python
# log
plt.plot(x, y)
plt.yscale('log')
plt.title('Logarithmic Scale')
plt.grid(True)
```
