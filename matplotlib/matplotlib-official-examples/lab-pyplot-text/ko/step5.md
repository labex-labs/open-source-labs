# 제목, X 축 레이블 및 Y 축 레이블 추가

`pyplot` 라이브러리의 `title()`, `xlabel()`, 그리고 `ylabel()` 메서드를 사용하여 그래프에 제목, X 축 레이블 및 Y 축 레이블을 추가할 수 있습니다. "Voltage vs Time"을 제목으로, "Time [s]"를 X 축 레이블로, "Voltage [mV]"를 Y 축 레이블로 추가합니다.

```python
plt.title(r'Voltage vs Time', fontsize=20)
plt.xlabel('Time [s]')
plt.ylabel('Voltage [mV]')
```
