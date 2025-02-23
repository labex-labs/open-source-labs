# Funktionskomposition mit Pipelines

Um zu beginnen, mit Pipelines zu programmieren, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Die `pipeFunctions`-Funktion führt eine links-nach-rechts-Funktionskomposition durch, indem sie `Array.prototype.reduce()` mit dem Spread-Operator (`...`) verwendet. Die erste (am linken Ende) Funktion kann einen oder mehrere Argumente akzeptieren, während die verbleibenden Funktionen unär sein müssen.

```js
const pipeFunctions = (...fns) =>
  fns.reduce(
    (f, g) =>
      (...args) =>
        g(f(...args))
  );
```

Hier ist ein Beispiel dafür, wie `pipeFunctions` verwendet werden kann, um eine neue Funktion `multiplyAndAdd5` zu erstellen, die zwei Zahlen multipliziert und dann 5 zum Ergebnis addiert:

```js
const add5 = (x) => x + 5;
const multiply = (x, y) => x * y;
const multiplyAndAdd5 = pipeFunctions(multiply, add5);
multiplyAndAdd5(5, 2); // 15
```

In diesem Beispiel ist `multiplyAndAdd5` eine neue Funktion, die zwei Argumente, `5` und `2`, annimmt und zuerst `multiply` auf sie anwendet, was `10` ergibt, und dann `add5` auf das Ergebnis anwendet, was `15` ergibt.
