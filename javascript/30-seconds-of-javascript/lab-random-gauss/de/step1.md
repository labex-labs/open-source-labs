# Generieren von Gaußschen Zufallszahlen mit der Box-Muller-Transformation

Um Gaußsche (normalverteilte) Zufallszahlen mit der Box-Muller-Transformation zu generieren, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie den bereitgestellten Codeausschnitt, der die Box-Muller-Transformation verwendet, um Zufallszahlen mit einer Gaußverteilung zu generieren.
3. Die `randomGauss()`-Funktion im Codeausschnitt generiert eine Zufallszahl mit einer Gaußverteilung.
4. Die Ausgabe der `randomGauss()`-Funktion ist eine Zahl zwischen 0 und 1.
5. Die Ausgabe kann für verschiedene Anwendungen verwendet werden, wie statistische Simulationen, Datenanalyse und maschinelles Lernen.

```js
const randomGauss = () => {
  const theta = 2 * Math.PI * Math.random();
  const rho = Math.sqrt(-2 * Math.log(1 - Math.random()));
  return (rho * Math.cos(theta)) / 10.0 + 0.5;
};
```

Beispielverwendung:

```js
randomGauss(); // 0.5
```
