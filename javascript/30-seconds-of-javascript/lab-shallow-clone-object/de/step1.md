# Wie man einen flachen Klon eines Objekts erstellt

Um einen flachen Klon eines Objekts zu erstellen, verwenden Sie `Object.assign()` und ein leeres Objekt (`{}`). Folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie den folgenden Code, um einen flachen Klon des ursprünglichen Objekts zu erstellen:

```js
const shallowClone = (obj) => Object.assign({}, obj);
```

3. Um das Objekt zu klonen, verwenden Sie die `shallowClone()`-Funktion wie folgt:

```js
const a = { x: true, y: 1 };
const b = shallowClone(a); // a!== b
```

In diesem Beispiel sind `a` und `b` zwei verschiedene Objekte, aber sie haben die gleichen Werte.
