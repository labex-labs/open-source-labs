# Verwendung von Hooks

> Das React-Projekt wurde bereits in der VM bereitgestellt. Im Allgemeinen müssen Sie nur Code in `App.js` hinzufügen.

Installieren Sie die Abhängigkeiten mit dem folgenden Befehl:

```bash
npm i
```

Funktionen, die mit `use` beginnen, werden als Hooks bezeichnet. `useState` ist ein von React bereitgestellter eingebauter Hook. Sie können andere eingebaute Hooks in der API-Referenz finden. Sie können auch eigene Hooks schreiben, indem Sie die vorhandenen kombinieren.

Hooks sind restriktiver als andere Funktionen. Sie können Hooks nur am Anfang Ihrer Komponenten (oder anderer Hooks) aufrufen. Wenn Sie `useState` in einer Bedingung oder einer Schleife verwenden möchten, extrahieren Sie eine neue Komponente und legen Sie sie dort.

Im vorherigen Beispiel hatte jeder `MyButton` seine eigene unabhängige `count`, und wenn jeder Button geklickt wurde, wechselte nur die `count` für den geklickten Button:

![Ohne Verwendung von Hooks](../assets/1.png)

Oft müssen Sie jedoch Komponenten dazu bringen, Daten zu teilen und immer zusammen zu aktualisieren.

Um beide `MyButton`-Komponenten die gleiche `count` anzuzeigen und zusammen zu aktualisieren, müssen Sie den Zustand von den einzelnen Buttons "nach oben" in die nächstgelegene Komponente verschieben, die alle enthält.

In diesem Beispiel ist es `MyApp`:

![Mit Verwendung von Hooks](../assets/2.png)

Wenn Sie jetzt auf einen der beiden Buttons klicken, ändert sich die `count` in `MyApp`, was die `count` in beiden `MyButton`-Komponenten ändert. Hier ist, wie Sie dies im Code ausdrücken können.

Zunächst verschieben Sie den Zustand von `MyButton` in `MyApp`:

```js
// App.js
export default function MyApp() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <div>
      <h1>Counters that update separately</h1>
      <MyButton />
      <MyButton />
    </div>
  );
}

function MyButton() {
  //... wir verschieben Code von hier...
}
```

Dann übergeben Sie den Zustand von `MyApp` an jede `MyButton` zusammen mit dem geteilten Click-Handler. Sie können Informationen an `MyButton` mithilfe von JSX-Klammern übergeben, genauso wie Sie es zuvor mit eingebauten Tags wie `<img>` getan haben:

```js
export default function MyApp() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <div>
      <h1>Counters that update together</h1>
      <MyButton count={count} onClick={handleClick} />
      <MyButton count={count} onClick={handleClick} />
    </div>
  );
}
```

Die Informationen, die Sie so übergeben, werden als `props` bezeichnet. Jetzt enthält die `MyApp`-Komponente den `count`-Zustand und den `handleClick`-Ereignishandler und übergibt beide als `props` an jeden der Buttons.

Schließlich ändern Sie `MyButton`, um die `props` zu lesen, die Sie von ihrer übergeordneten Komponente übergeben haben:

```js
function MyButton({ count, onClick }) {
  return <button onClick={onClick}>Clicked {count} times</button>;
}
```

Wenn Sie auf den Button klicken, wird der `onClick`-Handler ausgelöst. Der `onClick`-`prop` jedes Buttons wurde auf die `handleClick`-Funktion innerhalb von `MyApp` gesetzt, sodass der Code darin ausgeführt wird. Dieser Code ruft `setCount(count + 1)` auf, was die `count`-Zustandsvariable inkrementiert. Der neue `count`-Wert wird als `prop` an jeden Button übergeben, sodass alle den neuen Wert anzeigen. Dies wird als "Lifting des Zustands nach oben" bezeichnet. Indem Sie den Zustand nach oben verschieben, haben Sie ihn zwischen den Komponenten geteilt.

```js
import { useState } from "react";

export default function MyApp() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <div>
      <h1>Counters that update together</h1>
      <MyButton count={count} onClick={handleClick} />
      <MyButton count={count} onClick={handleClick} />
    </div>
  );
}

function MyButton({ count, onClick }) {
  return <button onClick={onClick}>Clicked {count} times</button>;
}
```

Um das Projekt auszuführen, verwenden Sie den folgenden Befehl. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.

```bash
npm start
```
