# Reordenar Argumentos de Funções com Flip

Para trocar a ordem dos argumentos de uma função, use a função `flip`. Esta função recebe uma função como argumento e retorna uma nova função que troca o primeiro e o último argumentos.

Para implementar `flip`:

- Use desestruturação de argumentos e um closure (fechamento) com argumentos variádicos.
- Use o operador spread (`...`) para o primeiro argumento, tornando-o o último argumento antes de aplicar o restante.

```js
const flip =
  (fn) =>
  (first, ...rest) =>
    fn(...rest, first);
```

Aqui está um exemplo de como usar `flip` para reordenar os argumentos de `Object.assign`:

```js
let a = { name: "John Smith" };
let b = {};

// Criar uma nova função que troca os argumentos de Object.assign
const mergeFrom = flip(Object.assign);

// Criar uma nova função que vincula o primeiro argumento a a
let mergePerson = mergeFrom.bind(null, a);

// Chamar a nova função com b como o segundo argumento
mergePerson(b); // b agora é igual a a

// Alternativamente, mesclar a e b sem usar a nova função
b = {};
Object.assign(b, a); // b agora é igual a a
```
