# Como Gerar uma String Alfanumérica Aleatória em JavaScript

Para gerar uma string aleatória de caracteres alfanuméricos em JavaScript, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Crie um novo array com o comprimento especificado usando `Array.from()`.
3.  Gere um número de ponto flutuante aleatório usando `Math.random()`.
4.  Converta o número em uma string alfanumérica usando `Number.prototype.toString()` com um valor `radix` de `36`.
5.  Remova a parte integral e o ponto decimal de cada número gerado usando `String.prototype.slice()`.
6.  Repita este processo quantas vezes forem necessárias, até `length`, usando `Array.prototype.some()`, pois ele produz uma string de comprimento variável a cada vez.
7.  Corte a string gerada se ela for maior que o `length` fornecido usando `String.prototype.slice()`.
8.  Retorne a string gerada.

Aqui está o código:

```js
const randomAlphaNumeric = (length) => {
  let s = "";
  Array.from({ length }).some(() => {
    s += Math.random().toString(36).slice(2);
    return s.length >= length;
  });
  return s.slice(0, length);
};
```

Você pode chamar a função `randomAlphaNumeric()` com o comprimento desejado como argumento. Por exemplo:

```js
randomAlphaNumeric(5); // '0afad'
```
