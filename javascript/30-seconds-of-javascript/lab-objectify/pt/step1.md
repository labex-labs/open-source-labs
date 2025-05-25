# Como Mapear um Array para um Objeto em JavaScript

Para mapear um array de objetos para um objeto em JavaScript, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Array.prototype.reduce()` para mapear o array para um objeto.
3.  Use o parâmetro `mapKey` para mapear as chaves do objeto e o parâmetro `mapValue` para mapear os valores.

Aqui está um trecho de código de exemplo que demonstra como usar a função `objectify` para mapear um array de objetos para um objeto:

```js
const objectify = (arr, mapKey, mapValue = (i) => i) =>
  arr.reduce((acc, item) => {
    acc[mapKey(item)] = mapValue(item);
    return acc;
  }, {});
```

Você pode então usar a função `objectify` para mapear um array de objetos para um objeto das seguintes maneiras:

```js
const people = [
  { name: "John", age: 42 },
  { name: "Adam", age: 39 }
];

// Mapear o array de objetos para um objeto usando a propriedade name como chaves
objectify(people, (p) => p.name.toLowerCase());
// Output: { john: { name: 'John', age: 42 }, adam: { name: 'Adam', age: 39 } }

// Mapear o array de objetos para um objeto usando a propriedade name como chaves e a propriedade age como valores
objectify(
  people,
  (p) => p.name.toLowerCase(),
  (p) => p.age
);
// Output: { john: 42, adam: 39 }
```
