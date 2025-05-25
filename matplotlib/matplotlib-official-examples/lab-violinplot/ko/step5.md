# 플롯 모양 사용자 정의

y 축 레이블을 제거하고 플롯에 제목을 추가하여 플롯의 모양을 사용자 정의합니다.

```python
for ax in axs.flat:
    ax.set_yticklabels([])

fig.suptitle("Violin Plotting Examples")
fig.subplots_adjust(hspace=0.4)
plt.show()
```
