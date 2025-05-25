# x 축 및 y 축의 제한 설정, 제목 및 그리드 추가

```python
ax.set_xlim(np.datetime64('1989-06-01'), np.datetime64('2023-01-01'))
fig.suptitle("Technology company stocks prices dollars (1990-2022)", ha="center")
ax.spines[:].set_visible(False)
ax.xaxis.tick_bottom()
ax.yaxis.tick_left()
ax.set_yscale('log')
ax.grid(True, 'major', 'both', ls='--', lw=.5, c='k', alpha=.3)
ax.tick_params(axis='both', which='both', labelsize='large',
               bottom=False, top=False, labelbottom=True,
               left=False, right=False, labelleft=True)
```
