# Como Iterar sobre as Próprias Propriedades de um Objeto em JavaScript

Para iterar sobre as próprias propriedades de um objeto e praticar a codificação, siga estes passos:

1. Abra o Terminal ou SSH.
2. Digite `node` para iniciar uma nova sessão do Node.js.
3. Use o método `Object.keys()` para recuperar um array das próprias propriedades do objeto.
4. Use o método `Array.prototype.forEach()` para percorrer cada propriedade e executar uma função fornecida.
5. A função fornecida deve aceitar três argumentos: o valor da propriedade, a chave da propriedade e o próprio objeto.
6. Use a função `forOwn()` com o objeto e a função fornecida para iterar sobre as propriedades do objeto.

Aqui está um trecho de código de exemplo:

```js
const forOwn = (obj, fn) =>
  Object.keys(obj).forEach((key) => fn(obj[key], key, obj));

forOwn({ foo: "bar", a: 1 }, (v) => console.log(v)); // 'bar', 1
```

Este código exibirá os valores das propriedades `foo` e `a` no console.
