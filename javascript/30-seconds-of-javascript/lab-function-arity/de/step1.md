# Wie man eine Funktion mit einer bestimmten Anzahl von Argumenten erstellt

Um eine Funktion zu erstellen, die eine bestimmte Anzahl von Argumenten akzeptiert und alle weiteren Argumente ignoriert, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.

2. Verwenden Sie den folgenden Code, um Ihre Funktion zu erstellen:

```js
const ary =
  (fn, n) =>
  (...args) =>
    fn(...args.slice(0, n));
```

3. Rufen Sie die gerade erstellte Funktion `ary` mit zwei Argumenten auf: die Funktion, für die Sie die Anzahl der Argumente begrenzen möchten (`fn`), und die Anzahl der Argumente, auf die Sie sie begrenzen möchten (`n`).

4. Nun können Sie die neue Funktion verwenden, um die Anzahl der Argumente für jede beliebige Funktion zu begrenzen. Dazu rufen Sie Ihre neue Funktion mit dem Spread-Operator (`...`) und den Argumenten auf, die Sie begrenzen möchten.

Hier ist ein Beispiel, wie Sie Ihre neue Funktion verwenden können:

```js
const firstTwoMax = ary(Math.max, 2);
[[2, 6, "a"], [6, 4, 8], [10]].map((x) => firstTwoMax(...x)); // [6, 6, 10]
```

In diesem Beispiel ist `firstTwoMax` eine neue Funktion, die die `Math.max`-Funktion auf die Akzeptanz von nur den ersten zwei Argumenten begrenzt. Die `map`-Methode wird verwendet, um die neue Funktion auf jedes Array in der äußeren Array anzuwenden und das Maximum der ersten beiden Elemente jedes inneren Arrays zurückzugeben.
