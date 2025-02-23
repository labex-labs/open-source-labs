# Debounce Promise

Um eine debounced-Funktion zu erstellen, die ein Promise zurückgibt und das Aufrufen der bereitgestellten Funktion bis mindestens `ms` Millisekunden seit dem letzten Aufruf verzögert, verwenden Sie die folgenden Schritte:

1. Wird die debounced-Funktion aufgerufen, so löschen Sie die aktuelle ausstehende Zeitüberschreitung mit `clearTimeout()`, und erstellen Sie dann mit `setTimeout()` eine neue Zeitüberschreitung, die das Aufrufen der Funktion bis mindestens `ms` Millisekunden verzögert.
2. Verwenden Sie `Function.prototype.apply()`, um den `this`-Kontext auf die Funktion anzuwenden und die erforderlichen Argumente bereitzustellen.
3. Erstellen Sie ein neues `Promise` und fügen Sie seine `resolve`- und `reject`-Callbacks der Warteschlange der ausstehenden Promises hinzu.
4. Wenn `setTimeout()` aufgerufen wird, kopieren Sie den aktuellen Stapel (da dieser sich zwischen dem Aufruf der bereitgestellten Funktion und ihrer Auflösung ändern kann), leeren Sie ihn und rufen Sie die bereitgestellte Funktion auf.
5. Wenn die bereitgestellte Funktion erfolgreich ist/fehlschlägt, lösen Sie alle Promises in der Warteschlange (bei Aufruf der Funktion kopiert) mit den zurückgegebenen Daten auf/ablehnen.
6. Lassen Sie das zweite Argument, `ms`, weg, um die Zeitüberschreitung auf einen Standardwert von `0` ms festzulegen.

Hier ist der Code für die `debouncePromise()`-Funktion:

```js
const debouncePromise = (fn, ms = 0) => {
  let timeoutId;
  const pending = [];
  return (...args) =>
    new Promise((res, rej) => {
      clearTimeout(timeoutId);
      timeoutId = setTimeout(() => {
        const currentPending = [...pending];
        pending.length = 0;
        Promise.resolve(fn.apply(this, args)).then(
          (data) => {
            currentPending.forEach(({ resolve }) => resolve(data));
          },
          (error) => {
            currentPending.forEach(({ reject }) => reject(error));
          }
        );
      }, ms);
      pending.push({ resolve: res, reject: rej });
    });
};
```

Hier ist ein Beispiel dafür, wie `debouncePromise()` verwendet werden kann:

```js
const fn = (arg) =>
  new Promise((resolve) => {
    setTimeout(resolve, 1000, ["resolved", arg]);
  });
const debounced = debouncePromise(fn, 200);
debounced("foo").then(console.log);
debounced("bar").then(console.log);
// Wird beidesmal ['resolved', 'bar'] ausgeben
```
