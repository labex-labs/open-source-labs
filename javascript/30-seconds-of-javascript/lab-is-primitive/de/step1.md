# Prüfung auf primitive Werte

Um das Programmieren zu üben, öffnen Sie das Terminal oder SSH und geben Sie `node` ein. Nachdem Sie das getan haben, können Sie überprüfen, ob ein Wert primitiv ist, indem Sie die folgenden Schritte ausführen:

1. Erstellen Sie aus dem Wert, den Sie überprüfen möchten, ein Objekt mit `Object(val)`.
2. Vergleichen Sie das erstellte Objekt mit dem ursprünglichen Wert mithilfe des strikt ungleichen Operators `!==`.
3. Wenn die beiden Werte nicht gleich sind, ist der ursprüngliche Wert primitiv.

Hier ist der Code für die `isPrimitive`-Funktion:

```js
const isPrimitive = (val) => Object(val) !== val;
```

Sie können diese Funktion mit den folgenden Werten testen:

```js
isPrimitive(null); // true
isPrimitive(undefined); // true
isPrimitive(50); // true
isPrimitive("Hello!"); // true
isPrimitive(false); // true
isPrimitive(Symbol()); // true
isPrimitive([]); // false
isPrimitive({}); // false
```

Wenn der Wert, den Sie überprüfen möchten, primitiv ist, wird die Funktion `true` zurückgeben. Andernfalls wird `false` zurückgegeben.
