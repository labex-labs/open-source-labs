# Criando uma Função com um Contexto Dado

Para criar uma função com um contexto dado, use a função `bind`. Primeiro, abra o Terminal/SSH e digite `node`.

A função `bind` cria uma nova função que invoca a função original com um contexto dado. Ela também pode, opcionalmente, adicionar quaisquer parâmetros adicionais fornecidos aos argumentos.

Para usar `bind`, passe a função original (`fn`) e o contexto desejado (`context`). Você também pode passar quaisquer parâmetros adicionais que devem ser vinculados à função (`...boundArgs`).

A função `bind` retorna uma nova função que usa `Function.prototype.apply()` para aplicar o `context` dado a `fn`. Ela também usa o operador spread (`...`) para adicionar quaisquer parâmetros adicionais fornecidos aos argumentos.

Aqui está um exemplo de uso de `bind`:

```js
const bind =
  (fn, context, ...boundArgs) =>
  (...args) =>
    fn.apply(context, [...boundArgs, ...args]);

function greet(greeting, punctuation) {
  return greeting + " " + this.user + punctuation;
}

const freddy = { user: "fred" };
const freddyBound = bind(greet, freddy);
console.log(freddyBound("hi", "!")); // 'hi fred!'
```

Neste exemplo, definimos uma função `greet` que recebe dois parâmetros (`greeting` e `punctuation`) e retorna uma string que concatena o `greeting`, a propriedade `user` do contexto atual (`this`) e a `punctuation`.

Em seguida, criamos um novo objeto (`freddy`) que tem uma propriedade `user` definida como `'fred'`.

Finalmente, criamos uma nova função (`freddyBound`) usando `bind`, passando a função `greet` e o objeto `freddy` como o contexto desejado. Podemos então chamar `freddyBound` com dois parâmetros adicionais (`'hi'` e `'!'`), que são passados para a função `greet` original, juntamente com o contexto `freddy` vinculado. A saída resultante é `'hi fred!'`.
