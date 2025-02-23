# Array auseinanderfalten

Um ein Array mit einer Iterationsfunktion und einem initialen Startwert zu erstellen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie eine `while`-Schleife und `Array.prototype.push()`, um die Iterationsfunktion wiederholt aufzurufen, bis sie `false` zurückgibt.
3. Die Iterationsfunktion sollte ein Argument (`seed`) akzeptieren und immer ein Array mit zwei Elementen ([`value`, `nextSeed`]) oder `false` zurückgeben, um zu beenden.

Verwenden Sie den folgenden Code, um die `unfold`-Funktion zu implementieren:

```js
const unfold = (fn, seed) => {
  let result = [],
    val = [null, seed];
  while ((val = fn(val[1]))) result.push(val[0]);
  return result;
};
```

Hier ist ein Beispiel dafür, wie die `unfold`-Funktion verwendet werden kann:

```js
var f = (n) => (n > 50 ? false : [-n, n + 10]);
unfold(f, 10); // [-10, -20, -30, -40, -50]
```

Dies erzeugt ein Array mit Werten, die von der Iterationsfunktion `f` ausgehend vom initialen Startwert von `10` generiert werden. Die Iterationsfunktion generiert bei jedem Schritt ein Array mit zwei Elementen: die Negation des aktuellen Startwerts und den nächsten Startwert, der um 10 erhöht wird. Der Prozess setzt sich fort, bis der Startwert größer als 50 ist, bei dem die Funktion `false` zurückgibt.
