# Como Converter um Caminho Tilde em um Caminho Absoluto no Node.js

Para começar a praticar a codificação em Node.js, abra o Terminal ou SSH e digite `node`. Para converter um caminho tilde em um caminho absoluto, use o seguinte código:

```js
const untildify = (str) =>
  str.replace(/^~($|\/|\\)/, `${require("os").homedir()}$1`);
```

O código usa `String.prototype.replace()` com uma expressão regular e `os.homedir()` para substituir o `~` no início do caminho pelo diretório home. Aqui está um exemplo de como usar a função `untildify`:

```js
untildify("~/node"); // returns '/Users/aUser/node'
```
