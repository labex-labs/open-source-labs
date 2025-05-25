# Função para Mapear Caracteres em uma String

Para usar esta função para mapear caracteres em uma string, siga estes passos:

- Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
- Use `String.prototype.split()` e `Array.prototype.map()` para chamar a função fornecida, `fn`, para cada caractere na string dada.
- Use `Array.prototype.join()` para recombinar o array de caracteres em uma nova string.
- A função de callback, `fn`, recebe três argumentos: o caractere atual, o índice do caractere atual e a string na qual `mapString` foi chamada.

Aqui está o código da função:

```js
const mapString = (str, fn) =>
  str
    .split("")
    .map((c, i) => fn(c, i, str))
    .join("");
```

Exemplo de uso:

```js
mapString("lorem ipsum", (c) => c.toUpperCase()); // 'LOREM IPSUM'
```
