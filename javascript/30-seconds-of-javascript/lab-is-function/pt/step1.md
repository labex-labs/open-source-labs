# Verificando se um Valor é uma Função

Para verificar se um valor é uma função, você pode usar o operador `typeof` com o primitivo `function`.

Aqui está um exemplo de uma função que verifica se um determinado valor é uma função:

```js
const isFunction = (val) => typeof val === "function";
```

Você pode usá-la assim:

```js
isFunction("x"); // false
isFunction((x) => x); // true
```

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.
