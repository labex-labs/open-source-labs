# Das Verständnis der Arität von einstelligen Funktionen

Um zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Die Arität von einstelligen Funktionen bezieht sich auf eine Funktion, die nur ein Argument annimmt und alle weiteren Argumente ignoriert.

Die bereitgestellte Funktion `fn` kann nur mit dem ersten angegebenen Argument aufgerufen werden. Um eine einstellige Funktion zu erstellen, verwenden Sie folgenden Code:

```js
const unary = (fn) => (val) => fn(val);
```

Ein Beispiel für die Verwendung von `unary` mit der `parseInt`-Funktion ist unten gezeigt:

```js
["6", "8", "10"].map(unary(parseInt)); // [6, 8, 10]
```
