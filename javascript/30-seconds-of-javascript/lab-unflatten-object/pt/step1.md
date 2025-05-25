# Como "Unflatten" (Desanexar) um Objeto em JavaScript

Para "unflatten" (desanexar) um objeto com caminhos para chaves em JavaScript, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.

2.  Use `Array.prototype.reduce()` aninhado para converter o caminho plano em um nó folha.

3.  Use `String.prototype.split()` para dividir cada chave com um delimitador de ponto e `Array.prototype.reduce()` para adicionar objetos em relação às chaves.

4.  Se o acumulador atual já contiver um valor em relação a uma chave específica, retorne seu valor como o próximo acumulador.

5.  Caso contrário, adicione o par chave-valor apropriado ao objeto acumulador e retorne o valor como o acumulador.

Aqui está o código para a função `unflattenObject`:

```js
const unflattenObject = (obj) =>
  Object.keys(obj).reduce((res, k) => {
    k.split(".").reduce(
      (acc, e, i, keys) =>
        acc[e] ||
        (acc[e] = isNaN(Number(keys[i + 1]))
          ? keys.length - 1 === i
            ? obj[k]
            : {}
          : []),
      res
    );
    return res;
  }, {});
```

Você pode usar a função `unflattenObject` para "unflatten" (desanexar) um objeto em JavaScript:

```js
unflattenObject({ "a.b.c": 1, d: 1 }); // { a: { b: { c: 1 } }, d: 1 }
unflattenObject({ "a.b": 1, "a.c": 2, d: 3 }); // { a: { b: 1, c: 2 }, d: 3 }
unflattenObject({ "a.b.0": 8, d: 3 }); // { a: { b: [ 8 ] }, d: 3 }
```
