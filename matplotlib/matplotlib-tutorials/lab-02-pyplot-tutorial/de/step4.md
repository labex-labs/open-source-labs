# Plotten mit kategorischen Variablen

Matplotlib ermöglicht es Ihnen, Plots mit kategorischen Variablen zu erstellen. Erstellen wir einen Balkendiagramm-, Streudiagramm- und Liniendiagramm mit kategorischen Variablen:

```python
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)

plt.suptitle('Categorical Plotting')
plt.show()
```

Erklärung:

- Wir erstellen eine Liste `names` mit drei kategorischen Werten und eine Liste `values`, die ihre entsprechenden Werte repräsentiert.
- Die `figure`-Funktion wird aufgerufen, um eine neue Figur mit einer bestimmten Größe zu erstellen.
- Wir verwenden die `subplot`-Funktion, um ein Gitter von Teilfiguren zu erstellen. In diesem Beispiel erstellen wir drei Teilfiguren, jede mit einem anderen Plottyp: Balkendiagramm, Streudiagramm und Liniendiagramm.
- Die `suptitle`-Funktion wird verwendet, um den Obertitel der Figur festzulegen.
