# Índice de Substrings

Para encontrar todos os índices de uma substring em uma string dada, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o método embutido `Array.prototype.indexOf()` para procurar por `searchValue` em `str`.
3.  Use `yield` para retornar o índice se o valor for encontrado e atualizar o índice, `i`.
4.  Use um loop `while` que terminará o gerador assim que o valor retornado de `Array.prototype.indexOf()` for `-1`.

Aqui está um exemplo de código para implementar os passos acima:

```js
const indexOfSubstrings = function* (str, searchValue) {
  let i = 0;
  while (true) {
    const r = str.indexOf(searchValue, i);
    if (r !== -1) {
      yield r;
      i = r + 1;
    } else return;
  }
};
```

Você pode testar a função com o seguinte código:

```js
[...indexOfSubstrings("tiktok tok tok tik tok tik", "tik")]; // [0, 15, 23]
[...indexOfSubstrings("tutut tut tut", "tut")]; // [0, 2, 6, 10]
[...indexOfSubstrings("hello", "hi")]; // []
```
