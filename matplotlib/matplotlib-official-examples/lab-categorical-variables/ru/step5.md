# Линейная диаграмма

Линейная диаграмма может быть использована для показа, как категориальная переменная меняется в течение времени. В этом примере мы будем использовать данные о уровнях счастья кошек и собак во время различных активностей.

```python
cat = ["bored", "happy", "bored", "bored", "happy", "bored"]
dog = ["happy", "happy", "happy", "happy", "bored", "bored"]
activity = ["combing", "drinking", "feeding", "napping", "playing", "washing"]
plt.plot(activity, dog, label="dog")
plt.plot(activity, cat, label="cat")
plt.title('Happiness Levels')
plt.xlabel('Activity')
plt.ylabel('Happiness')
plt.legend()
plt.show()
```
