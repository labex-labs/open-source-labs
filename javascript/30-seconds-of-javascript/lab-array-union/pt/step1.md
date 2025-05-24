# Como Encontrar a União de Dois Arrays em JavaScript

Para encontrar a união de dois arrays em JavaScript, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.

2.  A união de dois arrays retorna cada elemento que existe em qualquer um dos dois arrays pelo menos uma vez.

3.  Para obter a união de dois arrays, crie um `Set` com todos os valores de `a` e `b`, e converta-o em um array usando o método `Array.from()`.

Aqui está um exemplo de como implementar isso:

```js
const union = (a, b) => Array.from(new Set([...a, ...b]));

console.log(union([1, 2, 3], [4, 3, 2])); // Output: [1, 2, 3, 4]
```

No exemplo acima, a função `union()` recebe dois arrays, `[1, 2, 3]` e `[4, 3, 2]`, como argumentos e retorna a união dos dois arrays como um array `[1, 2, 3, 4]`.
