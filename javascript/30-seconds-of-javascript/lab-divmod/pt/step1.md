# Prática de Código: Quociente e Módulo da Divisão

Para praticar a codificação, abra o Terminal/SSH e digite `node`. Este código retorna um array que consiste no quociente e no resto dos números fornecidos.

Para obter o quociente da divisão `x / y`, use `Math.floor()`. Para obter o resto da divisão `x / y`, use o operador de módulo (`%`).

```js
const divmod = (x, y) => [Math.floor(x / y), x % y];
```

Por exemplo:

```js
divmod(8, 3); // [2, 2]
divmod(3, 8); // [0, 3]
divmod(5, 5); // [1, 0]
```
