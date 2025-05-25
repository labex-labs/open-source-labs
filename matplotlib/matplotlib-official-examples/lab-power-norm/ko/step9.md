# 제목 설정

이 단계에서는 각 플롯의 제목을 설정해야 합니다.

```python
axs[0, 0].set_title('Linear normalization')

for ax, gamma in zip(axs.flat[1:], gammas):
    ax.set_title(r'Power law $(\gamma=%1.1f)$' % gamma)
```
