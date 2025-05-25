# Gráfico de Linhas (Line Plot)

Um gráfico de linhas (line plot) pode ser usado para mostrar como uma variável categórica muda ao longo do tempo. Neste exemplo, usaremos dados sobre os níveis de felicidade de gatos e cães durante diferentes atividades.

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
