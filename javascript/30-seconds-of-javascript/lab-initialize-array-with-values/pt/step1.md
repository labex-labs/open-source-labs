# Função para Inicializar um Array com Valores Específicos

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.

Esta função inicializa um array com os valores especificados:

- Use o construtor `Array()` para criar um array com o comprimento desejado.
- Use `Array.prototype.fill()` para preenchê-lo com os valores desejados.
- Se nenhum valor for especificado, o padrão é `0`.

```js
const initializeArrayWithValues = (length, value = 0) =>
  Array(length).fill(value);
```

Exemplo de uso:

```js
initializeArrayWithValues(5, 2); // [2, 2, 2, 2, 2]
```
