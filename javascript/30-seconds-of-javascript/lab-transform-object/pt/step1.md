# Transformação de Objetos

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.

A função `transform` aplica uma função especificada em um acumulador e em cada chave do objeto, da esquerda para a direita. Veja como usá-la:

- Use `Object.keys()` para iterar sobre cada chave no objeto.
- Use `Array.prototype.reduce()` para aplicar a função especificada ao acumulador fornecido.

```js
const transform = (obj, fn, acc) =>
  Object.keys(obj).reduce((a, k) => fn(a, obj[k], k, obj), acc);
```

Aqui está um exemplo:

```js
transform(
  { a: 1, b: 2, c: 1 },
  (r, v, k) => {
    (r[v] || (r[v] = [])).push(k);
    return r;
  },
  {}
); // { '1': ['a', 'c'], '2': ['b'] }
```
