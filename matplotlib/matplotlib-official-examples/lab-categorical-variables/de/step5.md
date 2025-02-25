# Liniendiagramm

Ein Liniendiagramm kann verwendet werden, um zu zeigen, wie sich eine kategorische Variable über die Zeit ändert. In diesem Beispiel werden wir Daten über die Zufriedenheitsgrade von Katzen und Hunden während verschiedener Aktivitäten verwenden.

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
