# Algoritmo de Permutações de Strings

Para gerar todas as permutações de uma string que contém duplicatas, use o seguinte algoritmo:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2. Use recursão para criar todas as permutações possíveis da string dada.
3. Para cada letra na string dada, crie todas as permutações parciais para o restante de suas letras.
4. Use `Array.prototype.map()` para combinar a letra com cada permutação parcial.
5. Use `Array.prototype.reduce()` para combinar todas as permutações em um array.
6. Os casos base são para `String.prototype.length` igual a `2` ou `1`.
7. ⚠️ **AVISO**: O tempo de execução aumenta exponencialmente com cada caractere. Para strings com mais de 8 a 10 caracteres, o ambiente pode travar ao tentar resolver todas as diferentes combinações.

Aqui está o código JavaScript para o algoritmo:

```js
const stringPermutations = (str) => {
  if (str.length <= 2) return str.length === 2 ? [str, str[1] + str[0]] : [str];
  return str
    .split("")
    .reduce(
      (acc, letter, i) =>
        acc.concat(
          stringPermutations(str.slice(0, i) + str.slice(i + 1)).map(
            (val) => letter + val
          )
        ),
      []
    );
};
```

Você pode testar a função `stringPermutations` com o seguinte código:

```js
stringPermutations("abc"); // ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
```
