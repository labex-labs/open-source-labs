# 범례 추가 및 플롯 표시

가중치 없는 모델과 가중치가 부여된 모델을 구분하기 위해 플롯에 범례를 추가합니다. 그런 다음 플롯을 표시합니다.

```python
no_weights_handles, _ = no_weights.legend_elements()
weights_handles, _ = samples_weights.legend_elements()
ax.legend(
    [no_weights_handles[0], weights_handles[0]],
    ["no weights", "with weights"],
    loc="lower left",
)

ax.set(xticks=(), yticks=())
plt.show()
```
