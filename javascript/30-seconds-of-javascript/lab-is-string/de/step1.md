# Überprüfen, ob ein Wert ein String ist

Um zu überprüfen, ob ein Wert ein String ist, verwenden Sie das Schlüsselwort `typeof` gefolgt vom Wert, den Sie überprüfen möchten. Diese Methode funktioniert nur für primitive Strings.

Hier ist ein Beispielcode, der überprüft, ob ein bestimmter Wert ein String ist:

```js
const isString = (val) => typeof val === "string";
```

Sie können die `isString`-Funktion wie folgt verwenden:

```js
isString("10"); // true
```
