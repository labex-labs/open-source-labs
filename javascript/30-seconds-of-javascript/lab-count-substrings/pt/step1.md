# Como Contar Substrings em uma String usando JavaScript

Se você deseja praticar a codificação, abra o Terminal/SSH e digite `node`. Esta função JavaScript conta o número de ocorrências de uma substring especificada em uma determinada string.

Para usar esta função, siga estes passos:

1.  Declare uma função chamada `countSubstrings` que recebe dois parâmetros: `str` e `searchValue`.
2.  Inicialize duas variáveis: `count` e `i`.
3.  Use o método `Array.prototype.indexOf()` para procurar por `searchValue` em `str`.
4.  Se o valor for encontrado, incremente a variável `count` e atualize a variável `i`.
5.  Use um loop `while` que retorna assim que o valor retornado de `Array.prototype.indexOf()` for `-1`.
6.  Retorne a variável `count`.

Aqui está o código para a função `countSubstrings`:

```js
const countSubstrings = (str, searchValue) => {
  let count = 0,
    i = 0;
  while (true) {
    const r = str.indexOf(searchValue, i);
    if (r !== -1) [count, i] = [count + 1, r + 1];
    else return count;
  }
};
```

Você pode testar a função usando os exemplos abaixo:

```js
countSubstrings("tiktok tok tok tik tok tik", "tik"); // 3
countSubstrings("tutut tut tut", "tut"); // 4
```
