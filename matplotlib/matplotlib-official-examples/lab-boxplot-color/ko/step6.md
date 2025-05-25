# 수평 그리드 선 추가

마지막으로, `yaxis.grid()` 함수를 사용하여 박스 플롯에 수평 그리드 선을 추가합니다.

```python
for ax in [ax1, ax2]:
    ax.yaxis.grid(True)
    ax.set_xlabel('Three Separate Samples')
    ax.set_ylabel('Observed Values')

plt.show()
```
