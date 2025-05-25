# Truncar uma String em JavaScript

Para truncar uma string em JavaScript, você pode usar a função `truncateString`. Esta função recebe dois argumentos: `str` (a string a ser truncada) e `num` (o comprimento máximo da string truncada).

A função `truncateString` verifica se o comprimento de `str` é maior que `num`. Se for, a função trunca a string para o comprimento desejado e anexa `'...'` ao final. Caso contrário, ela retorna a string original.

Aqui está o código para a função `truncateString`:

```js
const truncateString = (str, num) =>
  str.length > num ? str.slice(0, num > 3 ? num - 3 : num) + "..." : str;
```

E aqui está um exemplo de como usar a função `truncateString`:

```js
truncateString("boomerang", 7); // 'boom...'
```
