# So wandelt man ein Array in ein Identitätsobjekt um

Wenn Sie sich in der Programmierung üben möchten, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Um ein Array von Werten in ein Objekt umzuwandeln, bei dem die gleichen Werte als Schlüssel und Werte verwendet werden, folgen Sie diesen Schritten:

1. Verwenden Sie `Array.prototype.map()`, um jedes Element auf ein Array von Schlüssel-Wert-Paaren abzubilden.
2. Verwenden Sie `Object.fromEntries()`, um das Array von Schlüssel-Wert-Paaren in ein Objekt umzuwandeln.

Hier ist der Code:

```js
const toIdentityObject = (arr) => Object.fromEntries(arr.map((v) => [v, v]));
```

Und hier ist ein Beispiel:

```js
toIdentityObject(["a", "b"]); // { a: 'a', b: 'b' }
```
