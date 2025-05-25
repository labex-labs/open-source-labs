# Como usar o Nor Lógico em JavaScript

Para começar a codificar em JavaScript, acesse o Terminal/SSH e digite `node`. O Nor lógico verifica se nenhum dos argumentos fornecidos é verdadeiro. Para retornar o inverso do ou lógico de dois valores, use o operador de negação lógica (`!`). Aqui está um exemplo:

```js
const nor = (a, b) => !(a || b);
```

E aqui estão algumas saídas:

```js
nor(true, true); // false
nor(true, false); // false
nor(false, false); // true
```
