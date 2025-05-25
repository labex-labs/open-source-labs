# Convertendo RGB para Objeto

Para converter uma string de cor `rgb()` em um objeto com os valores de cada cor, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `String.prototype.match()` para obter um array de 3 strings com os valores numéricos.
3.  Use `Array.prototype.map()` em combinação com `Number` para convertê-los em um array de valores numéricos.
4.  Use destruturação de array para armazenar os valores em variáveis nomeadas e criar um objeto apropriado a partir deles.

Aqui está o código que você pode usar:

```js
const toRGBObject = (rgbStr) => {
  const [red, green, blue] = rgbStr.match(/\d+/g).map(Number);
  return { red, green, blue };
};

toRGBObject("rgb(255, 12, 0)"); // {red: 255, green: 12, blue: 0}
```
