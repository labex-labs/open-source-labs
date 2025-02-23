# Logisches Xor

Um zu beginnen, mit der Programmierung zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Die logische Xor-Prüfung überprüft, ob nur einer der Argumente `true` ist. Um die logische Xor zu erstellen, verwenden Sie die Operatoren logisches Oder (`||`), Und (`&&`) und Nicht (`!`) auf den beiden angegebenen Werten. Hier ist ein Beispielcode dazu:

```js
const xor = (a, b) => (a || b) && !(a && b);
```

Hier sind die Ausgabewerte:

```js
xor(true, true); // false
xor(true, false); // true
xor(false, true); // true
xor(false, false); // false
```
