# Como Alterar a Luminosidade de uma Cor HSL

Para alterar o valor da luminosidade de uma string de cor `hsl()`, siga estes passos:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.

2. Use `String.prototype.match()` para obter um array de três strings com os valores numéricos da string `hsl()`.

3. Use `Array.prototype.map()` em combinação com `Number` para converter as strings em um array de valores numéricos.

4. Certifique-se de que o valor da luminosidade esteja dentro da faixa válida (entre `0` e `100`) usando `Math.max()` e `Math.min()`.

5. Use um template literal para criar uma nova string `hsl()` com o valor de luminosidade atualizado.

Aqui está um trecho de código de exemplo que implementa esses passos:

```js
const changeLightness = (delta, hslStr) => {
  const [hue, saturation, lightness] = hslStr.match(/\d+/g).map(Number);

  const newLightness = Math.max(
    0,
    Math.min(100, lightness + parseFloat(delta))
  );

  return `hsl(${hue}, ${saturation}%, ${newLightness}%)`;
};
```

Você pode então chamar a função `changeLightness()` com um valor delta e uma string `hsl()` para obter uma nova string `hsl()` com o valor de luminosidade atualizado. Por exemplo:

```js
changeLightness(10, "hsl(330, 50%, 50%)"); // 'hsl(330, 50%, 60%)'
changeLightness(-10, "hsl(330, 50%, 50%)"); // 'hsl(330, 50%, 40%)'
```
