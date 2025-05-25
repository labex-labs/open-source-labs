# 가장 불확실한 예측 시각화

가장 불확실한 상위 10 개 예측을 선택하고 표시합니다.

```python
pred_entropies = stats.distributions.entropy(lp_model.label_distributions_.T)

uncertainty_index = np.argsort(pred_entropies)[-10:]

f = plt.figure(figsize=(7, 5))
for index, image_index in enumerate(uncertainty_index):
    image = images[image_index]

    sub = f.add_subplot(2, 5, index + 1)
    sub.imshow(image, cmap=plt.cm.gray_r)
    plt.xticks([])
    plt.yticks([])
    sub.set_title(
        "예측: %i\n실제: %i" % (lp_model.transduction_[image_index], y[image_index])
    )

f.suptitle("소량의 레이블 데이터로 학습")
plt.show()
```
