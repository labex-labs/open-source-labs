# Como Converter uma String em um Array de Caracteres em JavaScript

Para converter uma string em um array de caracteres em JavaScript, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o operador spread (`...`) para converter a string em um array de caracteres.
3.  Defina uma função chamada `toCharArray` que recebe uma string como argumento e retorna um array de seus caracteres.
4.  Chame a função `toCharArray` com a string que você deseja converter como argumento.
5.  A função retornará um array de caracteres.

Aqui está o código:

```js
const toCharArray = (s) => [...s];

toCharArray("hello"); // ['h', 'e', 'l', 'l', 'o']
```
