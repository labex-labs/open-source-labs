# Plotar as Predições Mais Incertas

Selecionamos e mostramos as 10 predições mais incertas.

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
        "predizer: %i\nverdadeiro: %i" % (lp_model.transduction_[image_index], y[image_index])
    )

f.suptitle("Aprendizagem com pequena quantidade de dados rotulados")
plt.show()
```
