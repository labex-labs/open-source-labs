# Função para Ligar Método de Objeto

Para criar uma função que liga um método de objeto ao seu contexto e, opcionalmente, adiciona parâmetros adicionais, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Defina uma função que recebe três parâmetros: o contexto do objeto, a chave do método e quaisquer argumentos adicionais a serem adicionados.
3.  A função deve retornar uma nova função que usa `Function.prototype.apply()` para ligar o método ao contexto do objeto.
4.  Use o operador spread (`...`) para adicionar quaisquer parâmetros fornecidos adicionais aos argumentos.
5.  Aqui está um exemplo de implementação:

```js
const bindKey =
  (context, fn, ...boundArgs) =>
  (...args) =>
    context[fn].apply(context, [...boundArgs, ...args]);
```

6.  Para testar a função, crie um objeto com um método e ligue-o usando `bindKey()`. Em seguida, chame o método ligado com alguns argumentos.

```js
const freddy = {
  user: "fred",
  greet: function (greeting, punctuation) {
    return greeting + " " + this.user + punctuation;
  }
};
const freddyBound = bindKey(freddy, "greet");
console.log(freddyBound("hi", "!")); // 'hi fred!'
```
