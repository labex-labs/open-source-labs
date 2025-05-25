# Função para Converter Números em Sufixo Ordinal

Para converter um número em um sufixo ordinal, use a função `toOrdinalSuffix`.

- Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
- A função recebe um número como entrada e o retorna como uma string com o sufixo ordinal correto.
- Use o operador módulo (`%`) para encontrar os valores dos dígitos únicos e das dezenas.
- Encontre qual padrão ordinal os dígitos correspondem.
- Se o dígito for encontrado no padrão "teens", use o ordinal "teens".

```js
const toOrdinalSuffix = (num) => {
  const int = parseInt(num),
    digits = [int % 10, int % 100],
    ordinals = ["st", "nd", "rd", "th"],
    oPattern = [1, 2, 3, 4],
    tPattern = [11, 12, 13, 14, 15, 16, 17, 18, 19];
  return oPattern.includes(digits[0]) && !tPattern.includes(digits[1])
    ? int + ordinals[digits[0] - 1]
    : int + ordinals[3];
};
```

Aqui está um exemplo de como usar a função `toOrdinalSuffix`:

```js
toOrdinalSuffix("123"); // '123rd'
```
