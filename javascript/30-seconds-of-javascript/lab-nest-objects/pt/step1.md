# Como Aninhar Objetos Usando Recursão em JavaScript

Para aninhar objetos em um array plano recursivamente, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use recursão para aninhar objetos que estão ligados uns aos outros.
3.  Use `Array.prototype.filter()` para filtrar os itens onde o `id` corresponde ao `link`.
4.  Use `Array.prototype.map()` para mapear cada item para um novo objeto que possui uma propriedade `children` que aninha recursivamente os itens com base em quais são filhos do item atual.
5.  Omita o segundo argumento, `id`, para usar o padrão `null`, que indica que o objeto não está ligado a outro (ou seja, é um objeto de nível superior).
6.  Omita o terceiro argumento, `link`, para usar `'parent_id'` como a propriedade padrão que liga o objeto a outro por seu `id`.

Aqui está o código:

```js
const nest = (items, id = null, link = "parent_id") =>
  items
    .filter((item) => item[link] === id)
    .map((item) => ({ ...item, children: nest(items, item.id, link) }));
```

Para usar a função `nest()`, crie um array de objetos que tenham uma propriedade `id` e uma propriedade `parent_id` que os liga a outro objeto. Em seguida, chame a função `nest()` e passe o array como um argumento. A função retornará um novo array de objetos que são aninhados com base em sua propriedade `parent_id`.

Por exemplo:

```js
const comments = [
  { id: 1, parent_id: null },
  { id: 2, parent_id: 1 },
  { id: 3, parent_id: 1 },
  { id: 4, parent_id: 2 },
  { id: 5, parent_id: 4 }
];
const nestedComments = nest(comments);
// [{ id: 1, parent_id: null, children: [...] }]
```
