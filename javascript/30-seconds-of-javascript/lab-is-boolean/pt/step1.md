# Verificando se um Valor é Booleano

Para verificar se um valor é um primitivo booleano em JavaScript, use o operador `typeof` com o operador de comparação `===`.

```js
const isBoolean = (val) => typeof val === "boolean";
```

Aqui está um exemplo de como usar a função `isBoolean()` para verificar se um valor é booleano:

```js
isBoolean(null); // retorna false
isBoolean(false); // retorna true
```

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.
