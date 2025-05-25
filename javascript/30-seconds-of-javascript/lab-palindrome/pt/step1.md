# Como verificar se uma string é um palíndromo em JavaScript?

Para verificar se uma determinada string é um palíndromo em JavaScript, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Normalizar a string para minúsculas usando o método `String.prototype.toLowerCase()`.
3.  Remover caracteres não alfanuméricos da string usando o método `String.prototype.replace()` e uma expressão regular `[\W_]`.
4.  Dividir a string normalizada em caracteres individuais usando o operador spread (`...`).
5.  Inverter o array de caracteres usando o método `Array.prototype.reverse()`.
6.  Juntar o array invertido de caracteres em uma string usando o método `Array.prototype.join()`.
7.  Comparar a string invertida com a string normalizada para determinar se é um palíndromo.

Aqui está um trecho de código de exemplo que implementa os passos acima:

```js
const palindrome = (str) => {
  const normalizedStr = str.toLowerCase().replace(/[\W_]/g, "");
  return normalizedStr === [...normalizedStr].reverse().join("");
};

console.log(palindrome("taco cat")); // true
```

No exemplo acima, a função `palindrome()` recebe um argumento string e retorna `true` se a string for um palíndromo, e `false` caso contrário. A função usa os passos descritos acima para verificar se a string é um palíndromo.
