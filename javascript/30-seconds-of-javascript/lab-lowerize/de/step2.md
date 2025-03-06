# Zugriff auf Objektschlüssel (Object Keys)

Bevor wir die Schlüssel (keys) von Objekten transformieren können, müssen wir verstehen, wie wir auf sie zugreifen können. JavaScript bietet die Methode `Object.keys()`, die ein Array zurückgibt, das alle Schlüssel (keys) eines Objekts enthält.

Versuchen Sie in Ihrer Node.js interaktiven Shell Folgendes:

```javascript
Object.keys(user);
```

Sie sollten eine Ausgabe wie diese sehen:

```
[ 'Name', 'AGE', 'Email' ]
```

Jetzt versuchen wir, jeden Schlüssel (key) mit der Methode `toLowerCase()` in Kleinbuchstaben umzuwandeln. Wir können die Methode `map()` verwenden, um jeden Schlüssel zu transformieren:

```javascript
Object.keys(user).map((key) => key.toLowerCase());
```

Die Ausgabe sollte wie folgt aussehen:

```
[ 'name', 'age', 'email' ]
```

Toll! Wir haben jetzt ein Array mit allen Schlüsseln (keys), die in Kleinbuchstaben umgewandelt wurden. Allerdings müssen wir noch ein neues Objekt mit diesen Kleinbuchstaben-Schlüsseln und den ursprünglichen Werten erstellen. Dazu verwenden wir in dem nächsten Schritt die Methode `reduce()`.

Lassen Sie uns die Methode `reduce()` verstehen, bevor wir fortfahren. Diese Methode führt eine Reduzierfunktion (reducer function) für jedes Element des Arrays aus und liefert einen einzelnen Ausgabewert.

Hier ist ein einfaches Beispiel für `reduce()`:

```javascript
const numbers = [1, 2, 3, 4];
const sum = numbers.reduce((accumulator, currentValue) => {
  return accumulator + currentValue;
}, 0);

sum;
```

Die Ausgabe wird `10` sein, was die Summe aller Zahlen im Array ist. Die `0` in der `reduce()`-Methode ist der Anfangswert des Akkumulators (accumulator).
