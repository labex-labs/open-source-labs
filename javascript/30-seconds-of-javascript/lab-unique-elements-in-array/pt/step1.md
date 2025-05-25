# Como Encontrar Valores Únicos em um Array com JavaScript

Para encontrar todos os valores únicos em um array, você pode seguir estes passos em JavaScript:

1.  Crie um `Set` a partir do array fornecido para descartar valores duplicados.
2.  Use o operador spread (`...`) para converter o `Set` de volta para um array.

Aqui está um exemplo de trecho de código:

```js
const getUniqueValues = (arr) => [...new Set(arr)];
```

Você pode chamar a função e passar um array para ela, assim:

```js
getUniqueValues([1, 2, 2, 3, 4, 4, 5]); // [1, 2, 3, 4, 5]
```

Isso retornará um array com todos os valores únicos do array original, sem quaisquer duplicatas.
