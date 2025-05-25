# 로짓 스케일 플롯 생성

네 번째로 탐구할 스케일 변환 유형은 로짓 (logit) 입니다. 이 유형의 스케일은 0 과 1 로 제한된 데이터를 처리할 때 유용합니다. 로짓 스케일 플롯을 생성하려면 `set_yscale()` 메서드를 사용하고 문자열 `'logit'`을 전달합니다. 또한 플롯에 제목과 그리드를 추가합니다.

```python
# logit
plt.plot(x, y)
plt.yscale('logit')
plt.title('Logit Scale')
plt.grid(True)
```
