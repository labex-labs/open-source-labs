# Como Converter as Chaves de um Objeto para Maiúsculas em JavaScript

Para converter todas as chaves de um objeto para letras maiúsculas em JavaScript, siga estes passos:

1.  Use `Object.keys()` para obter um array das chaves do objeto.
2.  Use `Array.prototype.reduce()` para mapear o array para um objeto.
3.  Use `String.prototype.toUpperCase()` para converter as chaves para maiúsculas.

Aqui está o código:

```js
const upperize = (obj) =>
  Object.keys(obj).reduce((acc, k) => {
    acc[k.toUpperCase()] = obj[k];
    return acc;
  }, {});
```

Para testar a função, você pode chamá-la assim:

```js
upperize({ Name: "John", Age: 22 }); // { NAME: 'John', AGE: 22 }
```
