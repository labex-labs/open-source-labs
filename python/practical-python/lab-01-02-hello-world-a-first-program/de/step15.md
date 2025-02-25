# Ausgeben

Die `print`-Funktion erzeugt eine einzelne Zeile von Text mit den übergebenen Werten.

```python
print('Hello world!') # Gibt den Text 'Hello world!' aus
```

Sie können Variablen verwenden. Der ausgegebene Text wird der Wert der Variable sein, nicht der Name.

```python
x = 100
print(x) # Gibt den Text '100' aus
```

Wenn Sie mehr als einen Wert an `print` übergeben, werden sie durch Leerzeichen getrennt.

```python
name = 'Jake'
print('Mein Name ist', name) # Gibt den Text 'Mein Name ist Jake' aus
```

`print()` fügt immer ein Zeilenumbruch am Ende hinzu.

```python
print('Hello')
print('Mein Name ist', 'Jake')
```

Dies gibt aus:

```code
Hello
Mein Name ist Jake
```

Der zusätzliche Zeilenumbruch kann unterdrückt werden:

```python
print('Hello', end=' ')
print('Mein Name ist', 'Jake')
```

Dieser Code gibt jetzt aus:

```code
Hello Mein Name ist Jake
```
