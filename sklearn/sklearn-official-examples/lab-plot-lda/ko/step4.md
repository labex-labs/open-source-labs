# 결과 시각화

마지막으로, 각 분류기의 분류 정확도를 특징 개수의 함수로 플롯합니다. matplotlib 을 사용하여 플롯을 생성합니다.

```python
import matplotlib.pyplot as plt

features_samples_ratio = np.array(n_features_range) / n_train

plt.plot(
    features_samples_ratio,
    acc_clf1,
    linewidth=2,
    label="LDA",
    color="gold",
    linestyle="solid",
)
plt.plot(
    features_samples_ratio,
    acc_clf2,
    linewidth=2,
    label="LDA with Ledoit Wolf",
    color="navy",
    linestyle="dashed",
)
plt.plot(
    features_samples_ratio,
    acc_clf3,
    linewidth=2,
    label="LDA with OAS",
    color="red",
    linestyle="dotted",
)

plt.xlabel("n_features / n_samples")
plt.ylabel("분류 정확도")

plt.legend(loc="lower left")
plt.ylim((0.65, 1.0))
plt.suptitle(
    "LDA (선형 판별 분석) vs. "
    + "\n"
    + "Ledoit Wolf 을 사용한 LDA vs. "
    + "\n"
    + "OAS 를 사용한 LDA (1 개의 판별 특징)"
)
plt.show()
```
