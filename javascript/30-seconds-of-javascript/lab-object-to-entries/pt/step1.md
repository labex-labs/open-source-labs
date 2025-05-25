# Convertendo um Objeto para um Array de Pares Chave-Valor

Para converter um objeto em um array de pares chave-valor, use o método `Object.keys()` e o método `Array.prototype.map()`. Isso irá iterar sobre as chaves do objeto e produzir um array com pares chave-valor. Alternativamente, você pode usar o método `Object.entries()`, que fornece funcionalidade semelhante.

Aqui está um trecho de código de exemplo que mostra como converter um objeto em um array de pares chave-valor:

```js
const objectToEntries = (obj) => Object.keys(obj).map((k) => [k, obj[k]]);
```

Você pode usar a função `objectToEntries()` para converter um objeto em um array de pares chave-valor assim:

```js
objectToEntries({ a: 1, b: 2 }); // [ ['a', 1], ['b', 2] ]
```
