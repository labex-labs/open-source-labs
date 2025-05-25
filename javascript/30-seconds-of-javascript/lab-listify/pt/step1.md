# Como Mapear um Objeto para um Array em JavaScript

Para mapear um objeto para um array em JavaScript, você pode usar a função `listify()`. Veja como você pode fazer isso:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.

2.  Use `Object.entries()` para obter um array dos pares chave-valor do objeto.

3.  Use `Array.prototype.reduce()` para mapear o array para um objeto.

4.  Use `mapFn` para mapear as chaves e os valores do objeto e `Array.prototype.push()` para adicionar os valores mapeados ao array.

Aqui está o código para a função `listify()`:

```js
const listify = (obj, mapFn) =>
  Object.entries(obj).reduce((acc, [key, value]) => {
    acc.push(mapFn(key, value));
    return acc;
  }, []);
```

E aqui está um exemplo de como usá-la com um objeto chamado `people`:

```js
const people = { John: { age: 42 }, Adam: { age: 39 } };
listify(people, (key, value) => ({ name: key, ...value }));
// [ { name: 'John', age: 42 }, { name: 'Adam', age: 39 } ]
```

Com esta função, você pode facilmente mapear um objeto para um array em JavaScript.
