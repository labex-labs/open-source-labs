# Erstellen und Verschachteln von Komponenten

> Das React-Projekt wurde bereits in der VM bereitgestellt. Im Allgemeinen müssen Sie nur Code in `App.js` hinzufügen.

Installieren Sie die Abhängigkeiten mit dem folgenden Befehl:

```bash
npm i
```

React-Anwendungen bestehen aus Komponenten. Eine Komponente ist ein Teil der Benutzeroberfläche (UI), der seine eigene Logik und Erscheinung hat. Eine Komponente kann so klein wie eine Schaltfläche oder so groß wie eine ganze Seite sein.

React-Komponenten sind JavaScript-Funktionen, die Markup zurückgeben:

```js
// App.js
function MyButton() {
  return <button>I'm a button</button>;
}
```

Jetzt, nachdem Sie `MyButton` deklariert haben, können Sie es in eine andere Komponente verschachteln:

```js
// App.js
export default function MyApp() {
  return (
    <div>
      <h1>Welcome to my app</h1>
      <MyButton />
    </div>
  );
}
```

Beachten Sie, dass `<MyButton />` mit einem Großbuchstaben beginnt. So wissen Sie, dass es sich um eine React-Komponente handelt. React-Komponentennamen müssen immer mit einem Großbuchstaben beginnen, während HTML-Tags in Kleinbuchstaben sein müssen.

Das Schlüsselwort `export default` gibt die Hauptkomponente in der Datei an. Wenn Sie sich mit einem bestimmten JavaScript-Syntax-Abschnitt nicht vertraut sind, haben [MDN](https://developer.mozilla.org/en-US/docs/web/javascript/reference/statements/export) und [javascript.info](https://javascript.info/import-export) hervorragende Referenzen.

Führen Sie das Projekt mit dem folgenden Befehl aus. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.

```bash
npm start
```
