# 두 번째 서브플롯에 여러 줄 텍스트 추가

두 번째 서브플롯에서는 `text` 함수를 사용하여 여러 줄의 텍스트를 추가합니다. 텍스트의 위치, 크기, 수직 및 수평 정렬, 그리고 경계 상자 (bbox) 를 지정할 수 있습니다.

```python
ax1.text(0.29, 0.4, "Mat\nTTp\n123", size=18,
         va="baseline", ha="right", multialignment="left",
         bbox=dict(fc="none"))

ax1.text(0.34, 0.4, "Mag\nTTT\n123", size=18,
         va="baseline", ha="left", multialignment="left",
         bbox=dict(fc="none"))

ax1.text(0.95, 0.4, "Mag\nTTT$^{A^A}$\n123", size=18,
         va="baseline", ha="right", multialignment="left",
         bbox=dict(fc="none"))
```
