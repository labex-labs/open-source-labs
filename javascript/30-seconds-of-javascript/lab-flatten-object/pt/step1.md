# Achatar um Objeto

Para achatar um objeto com caminhos para as chaves, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use recursão para achatar o objeto.
3.  Use `Object.keys()` combinado com `Array.prototype.reduce()` para converter cada nó folha em um nó de caminho achatado.
4.  Se o valor de uma chave for um objeto, chame a função recursivamente com o `prefix` apropriado para criar o caminho usando `Object.assign()`.
5.  Caso contrário, adicione o par chave-valor com o prefixo apropriado ao objeto acumulador.
6.  Omita o segundo argumento, `prefix`, a menos que você queira que cada chave tenha um prefixo.

Aqui está um exemplo de implementação:

```js
const flattenObject = (obj, prefix = "") =>
  Object.keys(obj).reduce((acc, k) => {
    const pre = prefix.length ? `${prefix}.` : "";
    if (
      typeof obj[k] === "object" &&
      obj[k] !== null &&
      Object.keys(obj[k]).length > 0
    ) {
      Object.assign(acc, flattenObject(obj[k], pre + k));
    } else {
      acc[pre + k] = obj[k];
    }
    return acc;
  }, {});
```

Você pode usar a função `flattenObject` desta forma:

```js
flattenObject({ a: { b: { c: 1 } }, d: 1 }); // { 'a.b.c': 1, d: 1 }
```
