# 간단한 플롯 생성

Matplotlib 에서 간단한 플롯을 생성하려면 플롯하려는 숫자 목록을 제공해야 합니다. 이 경우, 일련의 숫자를 해당 인덱스에 대해 플롯하여 직선을 얻습니다. 마커 (원), 선 스타일 (실선) 및 색상 (빨간색) 을 설정하려면 형식 문자열 (여기서는 'o-r') 을 사용하십시오.

```python
plt.plot([1, 2, 3, 4], 'o-r')
plt.ylabel('some numbers')
plt.show()
```
