# 축 레이블 사용자 정의

글꼴 딕셔너리를 사용하여 플롯의 축 레이블도 사용자 정의할 수 있습니다. `xlabel()` 및 `ylabel()` 함수의 `fontdict` 매개변수를 저희 글꼴 딕셔너리로 설정합니다.

```python
plt.xlabel('Time (s)', fontdict=font)
plt.ylabel('Voltage (mV)', fontdict=font)
```
