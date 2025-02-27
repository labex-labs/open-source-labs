# Aktualisieren des Bildschirms

> Das React-Projekt wurde bereits in der VM bereitgestellt. Im Allgemeinen müssen Sie nur Code in `App.js` hinzufügen.

Installieren Sie die Abhängigkeiten mit dem folgenden Befehl:

```bash
npm i
```

Oft möchten Sie, dass Ihre Komponente einige Informationen "merkt" und anzeigt. Beispielsweise möchten Sie vielleicht zählen, wie oft eine Schaltfläche geklickt wird. Um dies zu tun, fügen Sie dem Zustand Ihrer Komponente hinzu.

Importieren Sie zunächst `useState` aus React:

```js
import { useState } from "react";
```

Jetzt können Sie eine Zustandsvariable innerhalb Ihrer Komponente deklarieren:

```js
function MyButton() {
  const [count, setCount] = useState(0);
  //...
```

Sie erhalten von `useState` zwei Dinge: den aktuellen Zustand (`count`) und die Funktion, mit der Sie ihn aktualisieren können (`setCount`). Sie können ihnen beliebige Namen geben, aber die Konvention ist es, `[etwas, setzeEtwas]` zu schreiben.

Die erste Zeit, wenn die Schaltfläche angezeigt wird, wird `count` `0` sein, da Sie `0` an `useState()` übergeben haben. Wenn Sie den Zustand ändern möchten, rufen Sie `setCount()` auf und übergeben ihm den neuen Wert. Beim Klicken dieser Schaltfläche wird der Zähler erhöht:

```js
function MyButton() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return <button onClick={handleClick}>Clicked {count} times</button>;
}
```

React wird Ihre Komponentenfunktion erneut aufrufen. Diesmal wird `count` `1` sein. Dann wird es `2` sein. Und so weiter.

Wenn Sie die gleiche Komponente mehrmals rendern, erhält jede eine eigene Zustand. Klicken Sie einzeln auf jede Schaltfläche:

```js
// App.js
import { useState } from "react";

export default function MyApp() {
  return (
    <div>
      <h1>Counters that update separately</h1>
      <MyButton />
      <MyButton />
    </div>
  );
}

function MyButton() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return <button onClick={handleClick}>Clicked {count} times</button>;
}
```

Beachten Sie, wie jede Schaltfläche ihren eigenen `count`-Zustand "merkt" und andere Schaltflächen nicht beeinträchtigt.

Um das Projekt auszuführen, verwenden Sie den folgenden Befehl. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.

```bash
npm start
```
