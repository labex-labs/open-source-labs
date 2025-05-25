# Converter HSL para Array

Para converter uma string de cor `hsl()` em um array de valores, siga estes passos:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2. Use `String.prototype.match()` para obter um array de 3 strings com os valores numéricos.
3. Use `Array.prototype.map()` em combinação com `Number` para convertê-los em um array de valores numéricos.

Aqui está o código para converter uma string de cor `hsl()` em um array de valores numéricos:

```js
const toHSLArray = (hslStr) => hslStr.match(/\d+/g).map(Number);
```

Exemplo de uso:

```js
toHSLArray("hsl(50, 10%, 10%)"); // [50, 10, 10]
```
