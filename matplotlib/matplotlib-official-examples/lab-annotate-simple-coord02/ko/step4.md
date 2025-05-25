# 도형 주석 추가

도형은 플롯의 특정 영역에 주의를 끌기 위해 사용할 수 있습니다. 이 단계에서는 x=1 과 x=3 사이의 영역을 강조 표시하기 위해 사각형을 추가합니다.

```python
# Add shape annotation
ax.axvspan(1, 3, facecolor='gray', alpha=0.2)
plt.show()
```
