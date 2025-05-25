# 두 클래스 결정 점수 시각화

이 단계에서는 두 클래스의 결정 점수를 시각화합니다. AdaBoost 분류기의 `decision_function` 메서드를 사용하여 데이터셋의 각 샘플에 대한 결정 점수를 얻습니다. 그런 다음 각 클래스의 결정 점수 히스토그램을 플롯합니다.

```python
# 두 클래스 결정 점수 플롯
twoclass_output = bdt.decision_function(X)
plot_range = (twoclass_output.min(), twoclass_output.max())
plt.subplot(122)
for i, n, c in zip(range(2), class_names, plot_colors):
    plt.hist(
        twoclass_output[y == i],
        bins=10,
        range=plot_range,
        facecolor=c,
        label="Class %s" % n,
        alpha=0.5,
        edgecolor="k",
    )
x1, x2, y1, y2 = plt.axis()
plt.axis((x1, x2, y1, y2 * 1.2))
plt.legend(loc="upper right")
plt.ylabel("샘플 수")
plt.xlabel("점수")
plt.title("결정 점수")

plt.tight_layout()
plt.subplots_adjust(wspace=0.35)
plt.show()
```
