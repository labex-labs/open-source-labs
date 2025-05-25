# Determinando se um Valor é um Objeto

Para determinar se um valor passado é um objeto, abra o Terminal/SSH e digite `node`. As seguintes etapas são executadas:

- O construtor `Object` cria um objeto wrapper (envoltório de objeto) para o valor fornecido.
- Se o valor for `null` ou `undefined`, um objeto vazio é criado e retornado.
- Se o valor não for `null` ou `undefined`, um objeto de um tipo correspondente ao valor fornecido é retornado.

Aqui está um exemplo de função que verifica se um valor é um objeto:

```js
const isObject = (obj) => obj === Object(obj);
```

Aqui estão alguns exemplos de uso da função `isObject`:

```js
isObject([1, 2, 3, 4]); // true
isObject([]); // true
isObject(["Hello!"]); // true
isObject({ a: 1 }); // true
isObject({}); // true
isObject(true); // false
```
