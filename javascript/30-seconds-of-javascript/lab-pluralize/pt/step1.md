# Pluralizar String (String Pluralize)

Para pluralizar uma palavra com base em um número fornecido, use a função `pluralize`. Comece abrindo o Terminal/SSH e digitando `node`. Esta função pode retornar a forma singular ou plural da palavra, dependendo do número de entrada. Você também pode fornecer um dicionário opcional para usar formas plurais personalizadas.

Para definir a função `pluralize`, use uma closure (fechamento) que recebe a `word` (palavra) e uma forma `plural` (plural) opcional. Se o `num` (número) de entrada for `-1` ou `1`, retorne a forma singular da `word`. Caso contrário, retorne a forma `plural`. Se nenhuma forma `plural` personalizada for fornecida, a função usará o padrão da `word` singular + `s`.

Se o primeiro argumento for um objeto, a função `pluralize` retorna uma nova função que pode usar o dicionário fornecido para resolver a forma plural correta da `word`.

Aqui está a função `pluralize` em ação:

```js
const pluralize = (val, word, plural = word + "s") => {
  const _pluralize = (num, word, plural = word + "s") =>
    [1, -1].includes(Number(num)) ? word : plural;
  if (typeof val === "object")
    return (num, word) => _pluralize(num, word, val[word]);
  return _pluralize(val, word, plural);
};
```

Você pode usar a função `pluralize` assim:

```js
pluralize(0, "apple"); // 'apples'
pluralize(1, "apple"); // 'apple'
pluralize(2, "apple"); // 'apples'
pluralize(2, "person", "people"); // 'people'
```

Se você tiver um dicionário de formas plurais personalizadas, pode criar uma função `autoPluralize` que usa automaticamente a forma plural correta para uma determinada `word`:

```js
const PLURALS = {
  person: "people",
  radius: "radii"
};
const autoPluralize = pluralize(PLURALS);
autoPluralize(2, "person"); // 'people'
```
