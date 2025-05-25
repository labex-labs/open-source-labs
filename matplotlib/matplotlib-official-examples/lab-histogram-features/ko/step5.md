# 히스토그램 사용자 정의

이 단계에서는 레이블, 제목을 추가하고 레이아웃을 조정하여 히스토그램을 사용자 정의합니다.

```python
ax.set_xlabel('Smarts')
ax.set_ylabel('Probability density')
ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')
fig.tight_layout()
plt.show()
```
