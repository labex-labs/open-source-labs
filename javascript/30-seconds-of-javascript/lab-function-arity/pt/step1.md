# Como Criar uma Função com um Número Específico de Argumentos

Para criar uma função que aceita um número específico de argumentos e ignora quaisquer argumentos adicionais, siga estes passos:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.

2. Use o seguinte código para criar sua função:

```js
const ary =
  (fn, n) =>
  (...args) =>
    fn(...args.slice(0, n));
```

3. Chame a função que você acabou de criar, `ary`, com dois argumentos: a função para a qual você deseja limitar os argumentos (`fn`) e o número de argumentos que você deseja limitar (`n`).

4. Agora você pode usar a nova função para limitar o número de argumentos para qualquer função que desejar. Para fazer isso, chame sua nova função com o operador spread (`...`) e os argumentos que você deseja limitar.

Aqui está um exemplo de como usar sua nova função:

```js
const firstTwoMax = ary(Math.max, 2);
[[2, 6, "a"], [6, 4, 8], [10]].map((x) => firstTwoMax(...x)); // [6, 6, 10]
```

Neste exemplo, `firstTwoMax` é uma nova função que limita a função `Math.max` a aceitar apenas os dois primeiros argumentos. O método `map` é usado para aplicar a nova função a cada array no array externo, retornando o máximo dos dois primeiros elementos de cada array interno.
