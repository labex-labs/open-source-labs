# Beschriftung von horizontalen Balkendiagrammen

Als nächstes erstellen wir ein horizontales Balkendiagramm und beschriften es mit der `bar_label`-Funktion. Wir verwenden die Daten aus dem vorherigen Schritt, aber diesmal generieren wir für jede Person einige zufällige Leistungsdaten.

```python
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

fig, ax = plt.subplots()

hbars = ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

# Label with specially formatted floats
ax.bar_label(hbars, fmt='%.2f')
ax.set_xlim(right=15)  # adjust xlim to fit labels

plt.show()
```
