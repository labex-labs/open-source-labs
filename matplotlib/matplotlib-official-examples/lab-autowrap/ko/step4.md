# 텍스트 배치 및 스타일 제어

Matplotlib 플롯에서 텍스트의 배치와 스타일을 제어할 수도 있습니다. 스크립트에 다음 코드를 추가해 보십시오.

```python
plt.text(2, 8, "Top Left", fontsize=12, color='red')
plt.text(8, 8, "Top Right", fontsize=12, color='blue')
plt.text(2, 2, "Bottom Left", fontsize=12, color='green')
plt.text(8, 2, "Bottom Right", fontsize=12, color='purple')
```

이렇게 하면 각기 다른 색상, 글꼴 크기 및 위치를 가진 네 개의 텍스트 요소가 플롯에 추가됩니다.
