# Conversão de HSL para Objeto

Para converter uma string de cor `hsl()` em um objeto com os valores numéricos de cada cor, siga estes passos:

- Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
- Use `String.prototype.match()` para obter um array de 3 strings com os valores numéricos.
- Converta as strings em um array de valores numéricos usando `Array.prototype.map()` em combinação com `Number`.
- Armazene os valores em variáveis nomeadas usando destructuring de array (desestruturação de array).
- Crie um objeto apropriado a partir das variáveis nomeadas.

```js
const toHSLObject = (hslStr) => {
  const [hue, saturation, lightness] = hslStr.match(/\d+/g).map(Number);
  return { hue, saturation, lightness };
};
```

Exemplo de uso:

```js
toHSLObject("hsl(50, 10%, 10%)"); // { hue: 50, saturation: 10, lightness: 10 }
```
