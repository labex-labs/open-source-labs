# Erstellen eines weiteren Textfelds

```python
plt.text(0.55, 0.6, "spam", size=50, rotation=-25.,
         ha="right", va="top",
         bbox=dict(boxstyle="square",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   )
         )
```

Wir erstellen ein weiteres Textfeld, das das Wort "Spam" enthält. Diesmal setzen wir den `boxstyle`-Parameter auf "square", um ein quadratisches Textfeld zu erstellen, und die `ha`- und `va`-Parameter auf "right" und "top", um den Text rechts oben im Textfeld auszurichten.
