# 화살표 주석 추가

이제 플롯에 화살표 주석을 추가합니다. 다음 코드는 첫 번째 데이터 포인트에서 두 번째 데이터 포인트로 화살표를 추가합니다.

```python
ax.annotate("", xy=(1, 3), xytext=(2, 4),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
```
