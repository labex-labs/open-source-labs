# Como Inverter a Capitalização (Swapcase) de uma String em JavaScript

Para inverter a capitalização (case) de uma string em JavaScript, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o operador spread (`...`) para converter a string de entrada `str` em um array de caracteres.
3.  Use `String.prototype.toLowerCase()` e `String.prototype.toUpperCase()` para converter caracteres minúsculos em maiúsculos e vice-versa.
4.  Use `Array.prototype.map()` para aplicar a transformação a cada caractere e `Array.prototype.join()` para combinar os caracteres de volta em uma string.
5.  Observe que inverter a capitalização (case) de uma string duas vezes pode não necessariamente resultar na string original.

Aqui está um trecho de código de exemplo que demonstra como inverter a capitalização (case) de uma string em JavaScript:

```js
const swapCase = (str) =>
  [...str]
    .map((c) => (c === c.toLowerCase() ? c.toUpperCase() : c.toLowerCase()))
    .join("");

swapCase("Hello world!"); // Output: 'hELLO WORLD!'
```
