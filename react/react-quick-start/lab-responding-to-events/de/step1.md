# Reaktion auf Ereignisse

> Das React-Projekt wurde bereits in der VM bereitgestellt. Im Allgemeinen müssen Sie nur Code in `App.js` hinzufügen.

Installieren Sie die Abhängigkeiten mit dem folgenden Befehl:

```bash
npm i
```

React ermöglicht es Ihnen, Ereignishandler zu Ihren JSX hinzuzufügen. Ereignishandler sind Ihre eigenen Funktionen, die in Reaktion auf Interaktionen wie Klicken, Hovern, Fokussieren von Formularfeldern usw. ausgelöst werden.

Um einen Ereignishandler hinzuzufügen, definieren Sie zunächst eine Funktion und übergeben Sie sie dann als [Prop](https://react.dev/learn/passing-props-to-a-component) an das passende JSX-Tag. Beispielsweise ist hier ein Button, der noch nichts tut:

```js
// App.js
export default function Button() {
  return <button>I don't do anything</button>;
}
```

Sie können es so gestalten, dass es eine Nachricht anzeigt, wenn ein Benutzer klickt, indem Sie die folgenden drei Schritte ausführen:

1. Deklarieren Sie eine Funktion namens `handleClick` innerhalb Ihrer `Button`-Komponente.
2. Implementieren Sie die Logik innerhalb dieser Funktion (verwenden Sie `alert`, um die Nachricht anzuzeigen).
3. Fügen Sie `onClick={handleClick}` zum `<button>`-JSX hinzu.

```js
export default function Button() {
  function handleClick() {
    alert("You clicked me!");
  }

  return <button onClick={handleClick}>Click me</button>;
}
```

Sie haben die `handleClick`-Funktion definiert und sie als Prop an `<button>` übergeben. `handleClick` ist ein Ereignishandler. Ereignishandlerfunktionen:

Werden normalerweise innerhalb Ihrer Komponenten definiert.
Haben Namen, die mit `handle` beginnen, gefolgt vom Namen des Ereignisses.

Um das Projekt auszuführen, verwenden Sie den folgenden Befehl. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.

```bash
npm start
```

Konventionell wird es üblich sein, Ereignishandler als `handle` gefolgt vom Ereignisnamen zu benennen. Sie werden oft `onClick={handleClick}`, `onMouseEnter={handleMouseEnter}` usw. sehen.

Alternativ können Sie einen Ereignishandler in der JSX inline definieren:

```js
<button onClick={function handleClick() {
  alert('You clicked me!');
}}>
```

Oder kürzer mit einer Arrow-Funktion:

```js
<button onClick={() => {
  alert('You clicked me!');
}}>
```

Alle diese Schreibweisen sind äquivalent. Inline-Ereignishandler sind für kurze Funktionen praktisch.
