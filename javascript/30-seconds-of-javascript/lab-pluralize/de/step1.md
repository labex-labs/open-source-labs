# String in Pluralform bringen

Um ein Wort basierend auf einer gegebenen Zahl in die Pluralform zu bringen, verwenden Sie die `pluralize`-Funktion. Öffnen Sie zunächst das Terminal/SSH und geben Sie `node` ein. Diese Funktion kann die Singular- oder Pluralform des Wortes zurückgeben, je nachdem, welche Eingabzahl übergeben wird. Sie können auch ein optionales Wörterbuch angeben, um benutzerdefinierte Pluralformen zu verwenden.

Um die `pluralize`-Funktion zu definieren, verwenden Sie eine Closure, die das `word` und eine optionale `plural`-Form akzeptiert. Wenn die Eingabe `num` entweder `-1` oder `1` ist, geben Sie die Singularform des `word` zurück. Andernfalls geben Sie die `plural`-Form zurück. Wenn keine benutzerdefinierte `plural`-Form angegeben wird, verwendet die Funktion als Standard die Singularform des `word` + `s`.

Wenn das erste Argument ein Objekt ist, gibt die `pluralize`-Funktion eine neue Funktion zurück, die das bereitgestellte Wörterbuch verwenden kann, um die richtige Pluralform des `word` zu ermitteln.

Hier ist die `pluralize`-Funktion im Einsatz:

```js
const pluralize = (val, word, plural = word + "s") => {
  const _pluralize = (num, word, plural = word + "s") =>
    [1, -1].includes(Number(num)) ? word : plural;
  if (typeof val === "object")
    return (num, word) => _pluralize(num, word, val[word]);
  return _pluralize(val, word, plural);
};
```

Sie können die `pluralize`-Funktion wie folgt verwenden:

```js
pluralize(0, "apple"); // 'Äpfel'
pluralize(1, "apple"); // 'Apfel'
pluralize(2, "apple"); // 'Äpfel'
pluralize(2, "person", "people"); // 'people'
```

Wenn Sie ein Wörterbuch mit benutzerdefinierten Pluralformen haben, können Sie eine `autoPluralize`-Funktion erstellen, die automatisch die richtige Pluralform für ein gegebenes `word` verwendet:

```js
const PLURALS = {
  person: "people",
  radius: "radii"
};
const autoPluralize = pluralize(PLURALS);
autoPluralize(2, "person"); // 'people'
```
