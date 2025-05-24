# Dicas para Codificação e Encontrar Chaves Comuns

Para praticar a codificação, abra o Terminal/SSH e digite `node`.

Para encontrar as chaves comuns entre dois objetos, siga estes passos:

1.  Use `Object.keys()` para obter as chaves do primeiro objeto.
2.  Use `Object.prototype.hasOwnProperty()` para verificar se o segundo objeto possui uma chave que está no primeiro objeto.
3.  Use `Array.prototype.filter()` para filtrar as chaves que não estão em ambos os objetos.

Aqui está um exemplo do código:

```js
const commonKeys = (obj1, obj2) =>
  Object.keys(obj1).filter((key) => obj2.hasOwnProperty(key));
```

Você pode testar o código com este exemplo:

```js
commonKeys({ a: 1, b: 2 }, { a: 2, c: 1 }); // ['a']
```
