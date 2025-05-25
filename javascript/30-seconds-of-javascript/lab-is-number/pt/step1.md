# Verificando se um Valor é um Número em JavaScript

Para verificar se um valor é um número em JavaScript, você pode usar o operador `typeof` para determinar se o valor é classificado como um primitivo do tipo número. Para evitar problemas com `NaN`, que tem um `typeof` igual a `number` e não é igual a si mesmo, você também pode verificar se o valor é igual a si mesmo usando `val === val`.

Aqui está um exemplo de função que verifica se um determinado valor é um número:

```js
const isNumber = (val) => typeof val === "number" && val === val;
```

Você pode usar esta função da seguinte forma:

```js
isNumber(1); // true
isNumber("1"); // false
isNumber(NaN); // false
```
