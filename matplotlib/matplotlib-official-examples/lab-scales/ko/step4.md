# 대칭 로그 스케일 플롯 생성

세 번째로 탐구할 스케일 변환 유형은 대칭 로그 (symmetrical logarithmic) 입니다. 이 유형의 스케일은 양수와 음수 값을 모두 포함하는 데이터를 처리할 때 유용합니다. 대칭 로그 스케일 플롯을 생성하려면 `set_yscale()` 메서드를 사용하고 문자열 `'symlog'`를 전달합니다. 또한 `linthresh` 매개변수를 `0.02`로 설정하여 0 주변에서 선형적으로 스케일링될 값의 범위를 지정합니다. 또한 플롯에 제목과 그리드를 추가합니다.

```python
# symmetric log
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthresh=0.02)
plt.title('Symmetrical Logarithmic Scale')
plt.grid(True)
```
