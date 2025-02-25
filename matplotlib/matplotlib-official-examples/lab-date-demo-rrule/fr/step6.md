# Tracez les données et définissez les repères de l'axe des x

Enfin, vous pouvez tracer les données à l'aide de la fonction `plot`, et définir les repères de l'axe des x à l'aide des fonctions de localisateur et de formateur de repères que vous avez définies précédemment.

```python
fig, ax = plt.subplots()
plt.plot(dates, s, 'o')
ax.xaxis.set_major_locator(loc)
ax.xaxis.set_major_formatter(formatter)
ax.xaxis.set_tick_params(rotation=30, labelsize=10)
plt.show()
```
