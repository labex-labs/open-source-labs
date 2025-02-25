# Diagramme en ligne

Un diagramme en ligne peut être utilisé pour montrer comment une variable catégorielle change au fil du temps. Dans cet exemple, nous utiliserons des données sur les niveaux de bonheur des chats et des chiens pendant différentes activités.

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
