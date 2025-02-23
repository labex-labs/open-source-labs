# Verwendung des logischen UND-Operators

Um zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Verwenden Sie dann den logischen UND (`&&`)-Operator, um zu überprüfen, ob beide Argumente `true` sind. Hier ist ein Beispielcode:

```js
const and = (a, b) => a && b;
and(true, true); // true
and(true, false); // false
and(false, false); // false
```
