# Convertendo String RGB para um Array

Para converter uma string de cor `rgb()` em um array de valores, siga estas etapas:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `String.prototype.match()` para obter um array de 3 strings com os valores numéricos.
3.  Use `Array.prototype.map()` em combinação com `Number` para convertê-los em um array de valores numéricos.

Aqui está o código que você pode usar:

```js
const toRGBArray = (rgbStr) => rgbStr.match(/\d+/g).map(Number);
```

Para testar a função, chame-a com uma string de cor `rgb()` como argumento, assim:

```js
toRGBArray("rgb(255, 12, 0)"); // [255, 12, 0]
```
