# Verificando a Igualdade Aproximada de Números em JavaScript

Para praticar a codificação, abra o Terminal/SSH e digite `node`. Este código verifica se dois números são aproximadamente iguais. Para fazer isso:

- Use o método `Math.abs()` para comparar a diferença absoluta dos dois valores com `epsilon`.
- Se você não fornecer um terceiro argumento, `epsilon`, a função usará um valor padrão de `0.001`.

Aqui está o código:

```js
const approximatelyEqual = (v1, v2, epsilon = 0.001) =>
  Math.abs(v1 - v2) < epsilon;
```

Para testar a função, você pode chamá-la com dois números como argumentos, assim:

```js
approximatelyEqual(Math.PI / 2.0, 1.5708); // true
```

Isso retornará `true` porque `Math.PI / 2.0` é aproximadamente igual a `1.5708` com um epsilon de `0.001`.
