# Como Reorganizar Argumentos de Funções em JavaScript

Para reorganizar argumentos de funções em JavaScript, você pode usar a função `rearg()`. Primeiro, crie uma função que invoca a função fornecida com seus argumentos organizados de acordo com os índices especificados. Você pode usar `Array.prototype.map()` para reordenar argumentos com base em `indexes`. Em seguida, use o operador spread (`...`) para passar os argumentos transformados para `fn`.

Aqui está um exemplo de como usar a função `rearg()`:

```js
const rearg =
  (fn, indexes) =>
  (...args) =>
    fn(...indexes.map((i) => args[i]));
```

Neste exemplo, usamos `rearg()` para criar uma nova função que reorganiza os argumentos de outra função.

```js
var rearged = rearg(
  function (a, b, c) {
    return [a, b, c];
  },
  [2, 0, 1]
);
rearged("b", "c", "a"); // ['a', 'b', 'c']
```

No código acima, criamos uma nova função `rearged` que reorganiza os argumentos da função `function(a, b, c) { return [a, b, c]; }`. O argumento `indexes` especifica a ordem na qual os argumentos devem ser reorganizados. Neste caso, queremos que o terceiro argumento venha primeiro, o primeiro argumento venha em segundo lugar e o segundo argumento venha em terceiro lugar. Quando chamamos `rearged('b', 'c', 'a')`, ele retorna `['a', 'b', 'c']`, que é o resultado de chamar a função original com os argumentos reorganizados.
