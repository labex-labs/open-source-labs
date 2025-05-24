# Verificando se uma Coleção está Vazia

Para verificar se uma coleção está vazia, você pode abrir o Terminal/SSH e digitar `node`. Este programa verifica se um valor é um objeto/coleção vazio, não possui propriedades enumeráveis ou é de qualquer tipo que não seja considerado uma coleção.

Para usar o programa, verifique se o valor fornecido é `null` ou se seu `length` (comprimento) é igual a `0`. Aqui está um exemplo de código:

```js
const isEmpty = (val) => val == null || !(Object.keys(val) || val).length;
```

Você pode então testar o programa usando os seguintes códigos:

```js
isEmpty([]); // true
isEmpty({}); // true
isEmpty(""); // true
isEmpty([1, 2]); // false
isEmpty({ a: 1, b: 2 }); // false
isEmpty("text"); // false
isEmpty(123); // true - type is not considered a collection
isEmpty(true); // true - type is not considered a collection
```
