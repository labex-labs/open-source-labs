# 결과 시각화

```python
ax1 = plt.subplot(211)
ax1.errorbar(
    x_values, scores.mean(axis=1), yerr=scores.std(axis=1), capsize=2, color="b"
)
ax1.set_ylabel("정확도", color="b")
ax1.tick_params("y", colors="b")

ax2 = ax1.twinx()
ax2.errorbar(
    x_values,
    amount_labeled.mean(axis=1),
    yerr=amount_labeled.std(axis=1),
    capsize=2,
    color="g",
)
ax2.set_ylim(bottom=0)
ax2.set_ylabel("레이블링된 샘플 수", color="g")
ax2.tick_params("y", colors="g")

ax3 = plt.subplot(212, sharex=ax1)
ax3.errorbar(
    x_values,
    amount_iterations.mean(axis=1),
    yerr=amount_iterations.std(axis=1),
    capsize=2,
    color="b",
)
ax3.set_ylim(bottom=0)
ax3.set_ylabel("반복 횟수")
ax3.set_xlabel("임계값")

plt.show()
```

Matplotlib 를 사용하여 실험 결과를 시각화합니다. 상단 그래프는 분류기가 학습 종료 시 사용 가능한 레이블링된 샘플 수와 분류기의 정확도를 보여줍니다. 하단 그래프는 샘플이 레이블링된 마지막 반복 횟수를 보여줍니다.
