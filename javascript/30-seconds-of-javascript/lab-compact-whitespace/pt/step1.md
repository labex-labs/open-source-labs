# Função para Compactar Espaços em Branco em uma String

Para compactar espaços em branco em uma string, use a função `compactWhitespace()`.

- Ela usa `String.prototype.replace()` com uma expressão regular para substituir todas as ocorrências de 2 ou mais caracteres de espaço em branco por um único espaço.
- A função recebe uma string como argumento e retorna a string compactada.

```js
const compactWhitespace = (str) => str.replace(/\s{2,}/g, " ");
```

Exemplo de uso:

```js
compactWhitespace("Lorem    Ipsum"); // 'Lorem Ipsum'
compactWhitespace("Lorem \n Ipsum"); // 'Lorem Ipsum'
```
