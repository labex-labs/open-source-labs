# Como Calcular o Produto de Valores Numéricos em JavaScript

Para calcular o produto de dois ou mais números ou arrays em JavaScript, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o método `Array.prototype.reduce()` para multiplicar cada valor com um acumulador, que deve ser inicializado com o valor `1`.
3.  Defina uma função chamada `prod` que recebe qualquer número de argumentos usando o operador spread (`...`). Dentro da função, aplique o método `reduce()` ao array de argumentos espalhados.
4.  A função retorna o resultado da multiplicação.

Aqui está um exemplo de como usar a função `prod`:

```js
const prod = (...arr) => [...arr].reduce((acc, val) => acc * val, 1);

prod(1, 2, 3, 4); // 24
prod(...[1, 2, 3, 4]); // 24
```

No exemplo acima, `prod(1, 2, 3, 4)` e `prod(...[1, 2, 3, 4])` ambos retornam `24`.
