# Verificando se um Valor é um Símbolo em JavaScript

Para verificar se um valor é um tipo primitivo símbolo em JavaScript, você pode usar o operador `typeof`. Aqui está um trecho de código de exemplo que você pode usar:

```js
const isSymbol = (val) => typeof val === "symbol";
```

Você pode chamar a função `isSymbol` e passar um símbolo como argumento para verificar se ela retorna `true`. Aqui está um exemplo:

```js
isSymbol(Symbol("x")); // true
```
