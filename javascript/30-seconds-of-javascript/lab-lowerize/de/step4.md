# Umgang mit Randfällen (Edge Cases)

Unsere Funktion funktioniert gut für einfache Objekte, aber wie sieht es mit komplexeren Fällen aus? Lassen Sie uns einige Randfälle (Edge Cases) untersuchen und sehen, wie unsere Funktion damit umgeht.

## Leere Objekte

Zunächst testen wir mit einem leeren Objekt:

```javascript
lowerizeKeys({});
```

Die Ausgabe sollte ein leeres Objekt sein:

```
{}
```

## Objekte mit verschachtelten Objekten

Was passiert, wenn das Objekt verschachtelte Objekte enthält? Lassen Sie uns das ausprobieren:

```javascript
const nestedObject = {
  User: {
    Name: "John",
    Contact: {
      EMAIL: "john@example.com",
      PHONE: "123-456-7890"
    }
  }
};

lowerizeKeys(nestedObject);
```

Die Ausgabe wird wie folgt aussehen:

```
{ user: { Name: 'John', Contact: { EMAIL: 'john@example.com', PHONE: '123-456-7890' } } }
```

Beachten Sie, dass nur der oberste Schlüssel (key) `User` in Kleinbuchstaben umgewandelt wird. Die Schlüssel (keys) innerhalb der verschachtelten Objekte bleiben unverändert.

Um verschachtelte Objekte zu verarbeiten, müssten wir unsere Funktion ändern, um alle Objekte rekursiv zu verarbeiten. Lassen Sie uns eine verbesserte Version erstellen:

```javascript
const deepLowerizeKeys = (obj) => {
  return Object.keys(obj).reduce((acc, key) => {
    const value = obj[key];
    // Check if the value is an object and not null
    const newValue =
      value && typeof value === "object" && !Array.isArray(value)
        ? deepLowerizeKeys(value)
        : value;

    acc[key.toLowerCase()] = newValue;
    return acc;
  }, {});
};
```

Diese verbesserte Funktion:

1. Prüft, ob jeder Wert ebenfalls ein Objekt ist (und kein Array oder null).
2. Wenn ja, ruft sie sich selbst rekursiv für das verschachtelte Objekt auf.
3. Andernfalls verwendet sie den ursprünglichen Wert.

Lassen Sie uns sie mit unserem verschachtelten Objekt testen:

```javascript
const deepLowerizedObject = deepLowerizeKeys(nestedObject);
deepLowerizedObject;
```

Jetzt sollten Sie sehen, dass alle Schlüssel (keys) in Kleinbuchstaben umgewandelt sind, auch in verschachtelten Objekten:

```
{ user: { name: 'John', contact: { email: 'john@example.com', phone: '123-456-7890' } } }
```

Gut gemacht! Sie haben eine fortschrittliche Funktion erstellt, die verschachtelte Objekte verarbeiten kann.
