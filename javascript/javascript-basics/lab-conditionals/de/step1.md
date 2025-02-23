# Bedingte Anweisungen

> Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.

Bedingte Anweisungen sind Codekonstrukte, die verwendet werden, um zu testen, ob ein Ausdruck `true` zurückgibt oder nicht. Eine sehr häufige Form von bedingten Anweisungen ist die `if...else`-Anweisung. Beispielsweise:

```js
let iceCream = "chocolate";
if (iceCream === "chocolate") {
  console.log("Yay, I love chocolate ice cream!");
} else {
  console.log("Awwww, but chocolate is my favorite…");
}
```

Der Ausdruck innerhalb von `if ()` ist der Test. Hier wird der strikte Gleichheitsoperator (wie oben beschrieben) verwendet, um die Variable `iceCream` mit dem String `chocolate` zu vergleichen, um zu sehen, ob die beiden gleich sind. Wenn dieser Vergleich `true` zurückgibt, wird der erste Codeblock ausgeführt. Wenn der Vergleich nicht `true` ist, wird stattdessen der zweite Codeblock – nach der `else`-Anweisung – ausgeführt.
