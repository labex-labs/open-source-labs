# 绘制最不确定的预测结果

我们挑选并展示前 10 个最不确定的预测结果。

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
        "predict: %i\ntrue: %i" % (lp_model.transduction_[image_index], y[image_index])
    )

f.suptitle("Learning with small amount of labeled data")
plt.show()
```
