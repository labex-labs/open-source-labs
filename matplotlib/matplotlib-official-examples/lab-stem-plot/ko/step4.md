# 플롯 사용자 정의

`bottom` 매개변수를 사용하여 기준선을 조정하여 플롯을 사용자 정의할 수 있습니다. 또한 `linefmt`, `markerfmt`, 및 `basefmt` 매개변수를 사용하여 플롯의 형식 속성을 조정할 수 있습니다.

```python
markerline, stemlines, baseline = plt.stem(
    x, y, linefmt='grey', markerfmt='D', bottom=1.1)
markerline.set_markerfacecolor('none')
plt.show()
```

이 코드는 회색 선 형식과 다이아몬드 모양 마커가 있는 플롯을 생성합니다. 기준선도 1.1 로 조정되었습니다.
