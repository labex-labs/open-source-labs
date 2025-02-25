# Etiquetado de diagramas de barras horizontales

A continuación, crearemos un diagrama de barras horizontales y lo etiquetaremos utilizando la función `bar_label`. Utilizaremos los datos del paso anterior, pero esta vez generaremos algunos datos de rendimiento aleatorios para cada persona.

```python
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

fig, ax = plt.subplots()

hbars = ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis()  # etiquetas leídas de arriba hacia abajo
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

# Etiquetar con floats con formato especial
ax.bar_label(hbars, fmt='%.2f')
ax.set_xlim(right=15)  # ajustar xlim para ajustar las etiquetas

plt.show()
```
