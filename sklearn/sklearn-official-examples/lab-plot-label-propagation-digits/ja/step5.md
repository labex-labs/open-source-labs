# 最も不確実な予測をプロットする

最も不確実な上位 10 件の予測を選択して表示します。

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
