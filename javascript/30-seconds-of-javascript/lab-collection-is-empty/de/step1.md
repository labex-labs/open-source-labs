# Überprüfen, ob eine Sammlung leer ist

Um zu überprüfen, ob eine Sammlung leer ist, können Sie die Konsole/SSH öffnen und `node` eingeben. Dieses Programm überprüft, ob ein Wert ein leeres Objekt/Sammlung ist, keine aufzählbaren Eigenschaften hat oder irgendein Typ ist, der nicht als Sammlung betrachtet wird.

Um das Programm zu verwenden, überprüfen Sie, ob der bereitgestellte Wert `null` ist oder ob seine `length` gleich `0` ist. Hier ist ein Beispielcode:

```js
const isEmpty = (val) => val == null || !(Object.keys(val) || val).length;
```

Sie können dann das Programm mit folgenden Codes testen:

```js
isEmpty([]); // true
isEmpty({}); // true
isEmpty(""); // true
isEmpty([1, 2]); // false
isEmpty({ a: 1, b: 2 }); // false
isEmpty("text"); // false
isEmpty(123); // true - Typ wird nicht als Sammlung betrachtet
isEmpty(true); // true - Typ wird nicht als Sammlung betrachtet
```
