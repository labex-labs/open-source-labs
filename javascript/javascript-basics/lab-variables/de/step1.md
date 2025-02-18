# Variablen

> Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Programmierung zu beginnen.

Variablen sind Container, die Werte speichern. Sie beginnen damit, eine Variable mit dem Schlüsselwort `let` zu deklarieren, gefolgt vom Namen, den Sie der Variable geben:

```js
let myVariable;
```

Ein Semikolon am Ende einer Zeile gibt an, wo eine Anweisung endet. Es ist nur erforderlich, wenn Sie Anweisungen in einer einzigen Zeile trennen müssen. Einige Leute sind der Meinung, dass es eine gute Praxis ist, am Ende jeder Anweisung ein Semikolon zu setzen. Es gibt andere Regeln dafür, wann Sie Semikolons verwenden sollten und wann nicht.

Sie können eine Variable fast beliebig benennen, aber es gibt einige Einschränkungen. Wenn Sie sich nicht sicher sind, können Sie [Ihren Variablennamen überprüfen](https://mothereff.in/js-variables), um zu sehen, ob er gültig ist.

JavaScript unterscheidet zwischen Groß- und Kleinschreibung. Das bedeutet, dass `myVariable` nicht dasselbe wie `myvariable` ist. Wenn Sie Probleme in Ihrem Code haben, überprüfen Sie die Groß- und Kleinschreibung!

Nachdem Sie eine Variable deklariert haben, können Sie ihr einen Wert zuweisen:

```js
myVariable = "Bob";
```

Außerdem können Sie beide Operationen in einer einzigen Zeile ausführen:

```js
let myVariable = "Bob";
```

Sie rufen den Wert ab, indem Sie den Variablennamen aufrufen:

```js
myVariable;
```

Nachdem Sie einer Variable einen Wert zugewiesen haben, können Sie ihn später im Code ändern:

```js
let myVariable = "Bob";
myVariable = "Steve";
```

Beachten Sie, dass Variablen Werte unterschiedlicher [Datentypen](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures) enthalten können:

| Variable                                                             | Erklärung                                                                                                                                                            | Beispiel                                                                                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| [String](https://developer.mozilla.org/en-US/docs/Glossary/String)   | Dies ist eine Zeichenfolge, die als String bezeichnet wird. Um anzuzeigen, dass der Wert ein String ist, setzen Sie ihn in einfache oder doppelte Anführungszeichen. | `let myVariable = 'Bob';` oder `let myVariable = "Bob";`                                                                              |
| [Number](https://developer.mozilla.org/en-US/docs/Glossary/Number)   | Dies ist eine Zahl. Zahlen haben keine Anführungszeichen um sie herum.                                                                                               | `let myVariable = 10;`                                                                                                                |
| [Boolean](https://developer.mozilla.org/en-US/docs/Glossary/Boolean) | Dies ist ein Wahr/Falsch-Wert. Die Wörter `true` und `false` sind spezielle Schlüsselwörter, die keine Anführungszeichen benötigen.                                  | `let myVariable = true;`                                                                                                              |
| [Array](https://developer.mozilla.org/en-US/docs/Glossary/Array)     | Dies ist eine Struktur, die es Ihnen ermöglicht, mehrere Werte in einer einzigen Referenz zu speichern.                                                              | `let myVariable = [1,'Bob','Steve',10];` Greifen Sie auf jedes Element des Arrays wie folgt zu: `myVariable[0]`, `myVariable[1]` usw. |
| [Object](https://developer.mozilla.org/en-US/docs/Glossary/Object)   | Dies kann alles sein. Alles in JavaScript ist ein Objekt und kann in einer Variable gespeichert werden. Halten Sie dies im Hinterkopf, während Sie lernen.           | `let myVariable = document.querySelector('h1');` Auch alle obigen Beispiele.                                                          |

Warum brauchen wir also Variablen? Variablen sind notwendig, um in der Programmierung etwas Interessantes zu tun. Wenn Werte nicht ändern könnten, könnten Sie nichts Dynamisches tun, wie z. B. eine Begrüßungsnachricht personalisieren oder ein Bild in einer Bildgalerie ändern.
