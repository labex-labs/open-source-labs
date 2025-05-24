# Como executar uma função para cada elemento de um array em ordem inversa

Para executar uma função para cada elemento de um array, começando pelo último elemento do array, siga estes passos:

1. Clone o array fornecido usando `Array.prototype.slice()`.
2. Inverta o array clonado usando `Array.prototype.reverse()`.
3. Use `Array.prototype.forEach()` para iterar sobre o array invertido.

Aqui está um trecho de código de exemplo:

```js
const forEachRight = (arr, callback) => arr.slice().reverse().forEach(callback);
```

Você pode testar a função executando o seguinte código:

```js
forEachRight([1, 2, 3, 4], (val) => console.log(val)); // '4', '3', '2', '1'
```

Para começar a codificar, abra o Terminal/SSH e digite `node`.
