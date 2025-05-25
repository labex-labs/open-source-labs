# Como Stringificar JSON Circular

Para stringificar um objeto JSON que contém referências circulares, siga estes passos:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2. Crie um `WeakSet` para armazenar e verificar os valores vistos usando `WeakSet.prototype.add()` e `WeakSet.prototype.has()`.
3. Use `JSON.stringify()` com uma função substituidora (replacer function) personalizada que omite valores já presentes em `seen` e adiciona novos valores, se necessário.
4. ⚠️ **AVISO:** Esta função encontra e remove referências circulares, o que causa perda de dados circulares no JSON serializado.

Aqui está o código para a função `stringifyCircularJSON`:

```js
const stringifyCircularJSON = (obj) => {
  const seen = new WeakSet();
  return JSON.stringify(obj, (key, value) => {
    if (value !== null && typeof value === "object") {
      if (seen.has(value)) return;
      seen.add(value);
    }
    return value;
  });
};
```

Para testar a função, você pode criar um objeto com uma referência circular e chamar `stringifyCircularJSON`:

```js
const obj = { n: 42 };
obj.obj = obj;
stringifyCircularJSON(obj); // '{"n": 42}'
```
