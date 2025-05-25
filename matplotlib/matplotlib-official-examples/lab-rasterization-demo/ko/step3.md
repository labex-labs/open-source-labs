# 네 개의 서브플롯이 있는 그림 생성

래스터화의 다양한 측면을 설명하기 위해 네 개의 서브플롯이 있는 그림을 생성합니다.

```python
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, layout="constrained")
```
