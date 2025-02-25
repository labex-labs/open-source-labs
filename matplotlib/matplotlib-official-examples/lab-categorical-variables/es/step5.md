# Gráfico de línea

Un gráfico de línea se puede utilizar para mostrar cómo una variable categórica cambia con el tiempo. En este ejemplo, usaremos datos sobre los niveles de felicidad de los gatos y los perros durante diferentes actividades.

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
