# Erstellen der Funktion zur Umwandlung in Kleinbuchstaben

Nachdem wir nun verstehen, wie man auf Objektschlüssel (Object Keys) zugreift und die `reduce()`-Methode verwendet, erstellen wir eine Funktion, die alle Schlüssel (keys) eines Objekts in Kleinbuchstaben umwandelt.

Definieren Sie in Ihrer Node.js interaktiven Shell die folgende Funktion:

```javascript
const lowerizeKeys = (obj) => {
  return Object.keys(obj).reduce((acc, key) => {
    acc[key.toLowerCase()] = obj[key];
    return acc;
  }, {});
};
```

Lassen Sie uns analysieren, was diese Funktion tut:

1. `Object.keys(obj)` ruft alle Schlüssel (keys) des Eingabeobjekts ab.
2. `.reduce()` transformiert diese Schlüssel in ein neues Objekt.
3. Für jeden Schlüssel (key) erstellen wir einen neuen Eintrag im Akkumulatorobjekt (`acc`) mit:
   - Dem Schlüssel, der mit `key.toLowerCase()` in Kleinbuchstaben umgewandelt wurde.
   - Dem ursprünglichen Wert aus dem Eingabeobjekt (`obj[key]`).
4. Wir beginnen mit einem leeren Objekt `{}` als Anfangswert für den Akkumulator.
5. Schließlich geben wir den Akkumulator zurück, der unser neues Objekt mit Kleinbuchstaben-Schlüsseln ist.

Jetzt testen wir unsere Funktion mit dem `user`-Objekt, das wir zuvor erstellt haben:

```javascript
const lowercaseUser = lowerizeKeys(user);
lowercaseUser;
```

Sie sollten die folgende Ausgabe sehen:

```
{ name: 'John', age: 30, email: 'john@example.com' }
```

Perfekt! Alle Schlüssel (keys) sind jetzt in Kleinbuchstaben.

Lassen Sie uns ein weiteres Beispiel versuchen, um sicherzustellen, dass unsere Funktion korrekt funktioniert:

```javascript
const product = {
  ProductID: 101,
  ProductName: "Laptop",
  PRICE: 999.99
};

lowerizeKeys(product);
```

Die Ausgabe sollte wie folgt aussehen:

```
{ productid: 101, productname: 'Laptop', price: 999.99 }
```

Unsere Funktion funktioniert korrekt für verschiedene Objekte mit unterschiedlichen Groß- und Kleinschreibungen der Schlüssel (keys).
