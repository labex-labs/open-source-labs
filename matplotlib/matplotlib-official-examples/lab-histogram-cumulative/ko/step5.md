# Figure 레이블 지정

이 단계에서는 figure 에 레이블을 지정합니다. 제목, 그리드 선, x 축 및 y 축 레이블을 추가합니다.

```python
fig.suptitle("Cumulative Distributions")
for ax in axs:
    ax.grid(True)
    ax.legend()
    ax.set_xlabel("Annual rainfall (mm)")
    ax.set_ylabel("Probability of occurrence")
    ax.label_outer()

plt.show()
```
