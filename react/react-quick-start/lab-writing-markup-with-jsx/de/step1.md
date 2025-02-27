# Markup mit JSX schreiben

> Das React-Projekt wurde bereits in der VM bereitgestellt. Im Allgemeinen müssen Sie nur Code in `App.js` hinzufügen.

Installieren Sie die Abhängigkeiten mit dem folgenden Befehl:

```bash
npm i
```

Die oben gezeigte Markupsyntax wird als JSX bezeichnet. Sie ist optional, aber die meisten React-Projekte verwenden JSX aus Bequemlichkeit.

JSX ist strenger als HTML. Sie müssen Tags wie `<br />` schließen. Ihr Komponent kann auch nicht mehrere JSX-Tags zurückgeben. Sie müssen sie in einen gemeinsamen Elternknoten umschließen, wie einen `<h1>...</h1>` oder einen leeren `<>...</>`-Wrapper:

```js
// App.js
export default function Profile() {
  return (
    <>
      <h1>Hedy Lamarr</h1>
    </>
  );
}
```

Wenn Sie viel HTML in JSX umwandeln müssen, können Sie einen [online-Converter](https://transform.tools/html-to-jsx) verwenden.

Führen Sie das Projekt mit dem folgenden Befehl aus. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.

```bash
npm start
```
