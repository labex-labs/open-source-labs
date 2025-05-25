# Função JavaScript para Verificar se um Objeto Possui uma Chave

Para verificar se um valor alvo existe em um objeto JavaScript, use a função `hasKey`.

A função recebe dois argumentos: `obj`, o objeto JSON para pesquisar, e `keys`, um array de chaves para verificar. Aqui estão os passos para verificar se o objeto possui a(s) chave(s) fornecida(s):

1.  Verifique se o array `keys` não está vazio. Se estiver vazio, retorne `false`.
2.  Use o método `Array.prototype.every()` para iterar sobre o array `keys` e verificar sequencialmente cada chave na profundidade interna do `obj`.
3.  Use o método `Object.prototype.hasOwnProperty()` para verificar se `obj` não possui a chave atual ou não é um objeto. Se qualquer uma dessas condições for verdadeira, interrompa a propagação e retorne `false`.
4.  Caso contrário, atribua o valor da chave a `obj` para usar na próxima iteração.
5.  Se o array `keys` foi iterado com sucesso, retorne `true`.

Aqui está o código para a função `hasKey`:

```js
const hasKey = (obj, keys) => {
  return (
    keys.length > 0 &&
    keys.every((key) => {
      if (typeof obj !== "object" || !obj.hasOwnProperty(key)) return false;
      obj = obj[key];
      return true;
    })
  );
};
```

Aqui estão alguns exemplos de como usar a função `hasKey`:

```js
let obj = {
  a: 1,
  b: { c: 4 },
  "b.d": 5
};

hasKey(obj, ["a"]); // true
hasKey(obj, ["b"]); // true
hasKey(obj, ["b", "c"]); // true
hasKey(obj, ["b.d"]); // true
hasKey(obj, ["d"]); // false
hasKey(obj, ["c"]); // false
hasKey(obj, ["b", "f"]); // false
```
