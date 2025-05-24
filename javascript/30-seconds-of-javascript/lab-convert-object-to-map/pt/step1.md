# Como Converter um Objeto em um Map

Para converter um objeto em um `Map`, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Object.entries()` para converter o objeto em um array de pares chave-valor.
3.  Use o construtor `Map` para converter o array em um `Map`.

Aqui está um trecho de código de exemplo:

```js
const objectToMap = (obj) => new Map(Object.entries(obj));
```

Você pode usar a função `objectToMap()` para converter um objeto em um `Map`. Por exemplo:

```js
objectToMap({ a: 1, b: 2 }); // Map {'a' => 1, 'b' => 2}
```
