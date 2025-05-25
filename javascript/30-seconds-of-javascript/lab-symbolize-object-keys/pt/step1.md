# Como Simbolizar Chaves de Objetos em JavaScript

Para simbolizar chaves de objetos em JavaScript, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o método `Object.keys()` para obter as chaves do objeto que você deseja simbolizar.
3.  Use o método `Array.prototype.reduce()` e `Symbol` para criar um novo objeto onde cada chave é convertida em um `Symbol`.
4.  Aqui está um exemplo de trecho de código:

```js
const symbolizeKeys = (obj) =>
  Object.keys(obj).reduce(
    (acc, key) => ({ ...acc, [Symbol(key)]: obj[key] }),
    {}
  );
```

5.  Para testar a função, chame `symbolizeKeys()` com seu objeto como argumento, assim:

```js
symbolizeKeys({ id: 10, name: "apple" });
// { [Symbol(id)]: 10, [Symbol(name)]: 'apple' }
```

Seguindo estes passos, você pode facilmente simbolizar as chaves de qualquer objeto em JavaScript.
