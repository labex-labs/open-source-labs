# Função para Verificar se uma String Começa com uma Substring

Para verificar se uma determinada string começa com uma substring de outra string, siga os passos abaixo:

- Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
- Use um loop `for...in` e o método `String.prototype.slice()` para obter cada substring da `word` dada, começando no início.
- Use o método `String.prototype.startsWith()` para verificar a substring atual em relação ao `text`.
- Se uma substring correspondente for encontrada, retorne-a. Caso contrário, retorne `undefined`.

Aqui está uma função JavaScript que faz isso:

```js
const startsWithSubstring = (text, word) => {
  for (let i in word) {
    const substr = word.slice(-i - 1);
    if (text.startsWith(substr)) return substr;
  }
  return undefined;
};
```

Você pode chamar esta função da seguinte forma:

```js
startsWithSubstring("/>Lorem ipsum dolor sit amet", "<br />"); // returns '/>'
```
