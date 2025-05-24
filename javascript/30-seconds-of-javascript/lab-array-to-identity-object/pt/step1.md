# Como converter um array em um objeto identidade

Se você deseja praticar a codificação, abra o Terminal/SSH e digite `node`. Para converter um array de valores em um objeto com os mesmos valores como chaves e valores, siga estes passos:

1.  Use `Array.prototype.map()` para mapear cada valor para um array de pares chave-valor.
2.  Use `Object.fromEntries()` para converter o array de pares chave-valor em um objeto.

Aqui está o código:

```js
const toIdentityObject = (arr) => Object.fromEntries(arr.map((v) => [v, v]));
```

E aqui está um exemplo:

```js
toIdentityObject(["a", "b"]); // { a: 'a', b: 'b' }
```
