# Uma Função que Chama ou Retorna Outra Função

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.

Aqui está uma função chamada `callOrReturn` que recebe um argumento e o chama se for uma função; caso contrário, ela o retorna. Veja como funciona:

- A função recebe dois parâmetros: `fn` e `...args`. `fn` é o argumento a ser verificado, e `...args` é a lista de argumentos a serem passados para a função, se ela for chamada.
- Ela usa o operador `typeof` para verificar se o argumento fornecido é uma função.
- Se o argumento for de fato uma função, ela chama a função usando o operador spread (`...`) para passar o restante dos argumentos fornecidos. Caso contrário, ela simplesmente retorna o argumento.
- Aqui está um exemplo de como usar a função `callOrReturn`:

```js
const callOrReturn = (fn, ...args) =>
  typeof fn === "function" ? fn(...args) : fn;

callOrReturn((x) => x + 1, 1); // 2
callOrReturn(1, 1); // 1
```

No primeiro exemplo, `callOrReturn(x => x + 1, 1)` chama a função `x => x + 1` com o argumento `1`, que retorna `2`. No segundo exemplo, `callOrReturn(1, 1)` simplesmente retorna `1`, pois não é uma função.
