# Funktionen

> In der VM wurde bereits `index.html` bereitgestellt.

[Funktionen](https://developer.mozilla.org/en-US/docs/Glossary/Function) sind eine Möglichkeit, Funktionalität zu verpacken, die Sie wiederverwenden möchten. Es ist möglich, einen Codeblock als Funktion zu definieren, die ausgeführt wird, wenn Sie im Code den Funktionsnamen aufrufen. Dies ist eine gute Alternative, um den gleichen Code wiederholt zu schreiben. Sie haben bereits einige Anwendungen von Funktionen gesehen.

Beispielsweise:

```js
let myVariable = document.querySelector("h1");
```

```js
alert("hello!");
```

Diese Funktionen, `document.querySelector` und `alert`, sind im Browser integriert.

> Klicken Sie bitte in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.

Wenn Sie etwas sehen, das wie ein Variablennamen aussieht, aber mit Klammern `()` folgt, ist es wahrscheinlich eine Funktion. Funktionen nehmen oft [Argumente](https://developer.mozilla.org/en-US/docs/Glossary/Argument): Datenstücke, die sie benötigen, um ihre Aufgabe zu erledigen. Argumente werden in die Klammern gesetzt und durch Kommas getrennt, wenn es mehr als ein Argument gibt.

Beispielsweise macht die `alert()`-Funktion eine Pop-up-Box im Browserfenster erscheinen, aber wir müssen ihr einen String als Argument geben, um der Funktion mitzuteilen, welche Nachricht angezeigt werden soll.

Sie können auch Ihre eigenen Funktionen definieren.

Im nächsten Beispiel erstellen wir eine einfache Funktion, die zwei Zahlen als Argumente nimmt und sie miteinander multipliziert:

> Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um zu beginnen, zu programmieren.

```js
function multiply(num1, num2) {
  let result = num1 * num2;
  return result;
}
```

Versuchen Sie, dies in der Konsole auszuführen; testen Sie dann mit mehreren Argumenten. Beispielsweise:

```js
multiply(4, 7);
multiply(20, 20);
multiply(0.5, 3);
```

> **Hinweis:** Der [`return`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return)-Befehl sagt dem Browser, die Variable `result` aus der Funktion zurückzugeben, sodass sie verwendet werden kann. Dies ist notwendig, da Variablen, die innerhalb von Funktionen definiert werden, nur innerhalb dieser Funktionen verfügbar sind. Dies wird als Variablenbereich bezeichnet. (Weitere Informationen zu [Variablenbereich](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#variable_scope).)
