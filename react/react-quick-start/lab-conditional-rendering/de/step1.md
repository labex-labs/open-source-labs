# Bedingtes Rendern

> Das React-Projekt wurde bereits in der VM bereitgestellt. Im Allgemeinen müssen Sie nur Code in `App.js` hinzufügen.

Installieren Sie die Abhängigkeiten mit dem folgenden Befehl:

```bash
npm i
```

In React gibt es keine spezielle Syntax zum Schreiben von Bedingungen. Stattdessen verwenden Sie die gleichen Techniken wie bei der Schreibung von regulärem JavaScript-Code. Beispielsweise können Sie eine `if`-Anweisung verwenden, um JSX bedingt einzuschließen:

```js
if (isPacked) {
  return <li className="item">{name} ✔</li>;
}
return <li className="item">{name}</li>;
```

Wenn Sie kompakteren Code bevorzugen, können Sie den bedingten `?`-Operator verwenden. Anders als `if` funktioniert er innerhalb von JSX:

```js
return <li className="item">{isPacked ? name + " ✔" : name}</li>;
```

Wenn Sie den else-Zweig nicht benötigen, können Sie auch eine kürzere logische `&&`-Syntax verwenden:

```js
return <li className="item">{isPacked && name + " ✔"}</li>;
```

Wenn die `isPacked`-Eigenschaft `true` ist, gibt dieser Code einen anderen JSX-Baum zurück. Mit dieser Änderung erhalten einige der Elemente ein Häkchen am Ende:

```js
// App.js
function Item({ name, isPacked }) {
  if (isPacked) {
    return <li className="item">{name} ✔</li>;
  }
  return <li className="item">{name}</li>;
}

export default function PackingList() {
  return (
    <section>
      <h1>Sally Ride's Packing List</h1>
      <ul>
        <Item isPacked={true} name="Space suit" />
        <Item isPacked={true} name="Helmet with a golden leaf" />
        <Item isPacked={false} name="Photo of Tam" />
      </ul>
    </section>
  );
}
```

Führen Sie das Projekt mit dem folgenden Befehl aus. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.

```bash
npm start
```
