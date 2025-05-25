# Verificando se um Valor é uma String

Para verificar se um valor é uma string, use a palavra-chave `typeof` seguida pelo valor que você deseja verificar. Este método funciona apenas para strings primitivas.

Aqui está um exemplo de código que verifica se um determinado valor é uma string:

```js
const isString = (val) => typeof val === "string";
```

Você pode usar a função `isString` desta forma:

```js
isString("10"); // true
```
