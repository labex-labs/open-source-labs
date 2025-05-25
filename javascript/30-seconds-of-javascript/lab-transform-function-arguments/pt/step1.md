# Transformar Argumentos de Funções

Para transformar argumentos de funções, use a função `overArgs`, que cria uma nova função que invoca a função fornecida com seus argumentos transformados.

- Para transformar os argumentos, use `Array.prototype.map()` em combinação com o operador spread (`...`) e passe os argumentos transformados para `fn`.

```js
const overArgs =
  (fn, transforms) =>
  (...args) =>
    fn(...args.map((val, i) => transforms[i](val)));
```

- Para testar a função `overArgs`, crie uma função de exemplo e um array de transformações, então chame a nova função com argumentos.

```js
const square = (n) => n * n;
const double = (n) => n * 2;

const fn = overArgs((x, y) => [x, y], [square, double]);
fn(9, 3); // [81, 6]
```

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.
