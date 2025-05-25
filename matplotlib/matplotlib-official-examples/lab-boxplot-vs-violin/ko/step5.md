# 그리드 선 및 레이블 추가

수평 그리드 선을 추가하고, x-레이블과 y-레이블을 플롯에 설정합니다.

```python
for ax in axs:
    ax.yaxis.grid(True)
    ax.set_xticks([y + 1 for y in range(len(all_data))], labels=['x1', 'x2', 'x3', 'x4'])
    ax.set_xlabel('Four separate samples')
    ax.set_ylabel('Observed values')
```
