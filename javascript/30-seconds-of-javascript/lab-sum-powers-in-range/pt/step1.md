# Função para Calcular a Soma das Potências em um Intervalo Determinado

Para calcular a soma das potências de todos os números dentro de um intervalo especificado (incluindo ambos os pontos finais), use a seguinte função:

```js
const sumPower = (end, power = 2, start = 1) =>
  Array(end + 1 - start)
    .fill(0)
    .map((x, i) => (i + start) ** power)
    .reduce((a, b) => a + b, 0);
```

Veja como você pode usar esta função:

- Chame `sumPower(end)` para calcular a soma dos quadrados de todos os números de 1 até `end`.
- Chame `sumPower(end, power)` para calcular a soma das potências de ordem `power` de todos os números de 1 até `end`.
- Chame `sumPower(end, power, start)` para calcular a soma das potências de ordem `power` de todos os números de `start` até `end`.

Observe que os segundo e terceiro argumentos (`power` e `start`) são opcionais e, por padrão, são `2` e `1`, respectivamente, se não forem fornecidos.

Exemplo:

```js
sumPower(10); // Retorna 385 (soma dos quadrados dos números de 1 a 10)
sumPower(10, 3); // Retorna 3025 (soma dos cubos dos números de 1 a 10)
sumPower(10, 3, 5); // Retorna 2925 (soma dos cubos dos números de 5 a 10)
```
