# 축 레이블 및 눈금 레이블 추가

`figtext`를 사용하여 x 및 y 축 레이블을 추가합니다. `spines`를 사용하여 상단 및 오른쪽 스파인을 숨깁니다. `set_xticks` 및 `set_yticks`를 사용하여 사용자 정의 눈금 위치 및 레이블을 설정합니다.

```python
fig.text(0.9, 0.05, '$x$')
fig.text(0.1, 0.9, '$y$')

ax.spines[['top', 'right']].set_visible(False)
ax.set_xticks([a, b], labels=['$a$', '$b$'])
ax.set_yticks([])
```
