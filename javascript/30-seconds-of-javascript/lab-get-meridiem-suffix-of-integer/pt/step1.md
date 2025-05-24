# Como Obter o Sufixo Meridiano de um Inteiro

Para começar a codificar, abra o Terminal/SSH e digite `node`.

Aqui está uma função que converte um inteiro em uma string de formato de 12 horas com um sufixo meridiano.

Para fazer isso, use o operador módulo (`%`) e verificações condicionais.

```js
const getMeridiemSuffixOfInteger = (num) => {
  if (num === 0 || num === 24) {
    return "12am";
  } else if (num === 12) {
    return "12pm";
  } else if (num < 12) {
    return num + "am";
  } else {
    return (num % 12) + "pm";
  }
};
```

Aqui estão alguns exemplos de como usar esta função:

```js
getMeridiemSuffixOfInteger(0); // '12am'
getMeridiemSuffixOfInteger(11); // '11am'
getMeridiemSuffixOfInteger(13); // '1pm'
getMeridiemSuffixOfInteger(25); // '1pm'
```

Esta função recebe um inteiro como argumento e retorna uma string com o sufixo meridiano.
