# Anpassen des Diagrammstils

Wir können den Stil unseres Diagramms ändern, um es visuell ansprechender zu gestalten. Folgen Sie diesen Schritten:

1. Drucken Sie die Liste der verfügbaren Stile mit `print(plt.style.available)`.

```python
print(plt.style.available)
```

2. Wählen Sie einen Stil und wenden Sie ihn mit `plt.style.use(style_name)` an.

```python
plt.style.use('fivethirtyeight')
```

3. Zeigen wir das Diagramm erneut an.

```python
fig, ax = plt.subplots()
ax.barh(group_names, group_data)
```
