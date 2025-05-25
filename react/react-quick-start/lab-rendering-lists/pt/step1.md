# Renderização de Listas

> O projeto React já foi fornecido na VM. Em geral, você só precisa adicionar código ao `App.js`.

Por favor, use o seguinte comando para instalar as dependências:

```bash
npm i
```

Você dependerá de recursos do JavaScript, como o loop `for` e a função `map()` de array para renderizar listas de componentes.

Por exemplo, digamos que você tenha um array de produtos:

```js
const products = [
  { title: "Cabbage", id: 1 },
  { title: "Garlic", id: 2 },
  { title: "Apple", id: 3 }
];
```

Dentro do seu componente, use a função `map()` para transformar um array de produtos em um array de itens `<li>`:

```js
const listItems = products.map((product) => (
  <li key={product.id}>{product.title}</li>
));

return <ul>{listItems}</ul>;
```

Observe como `<li>` tem um atributo `key`. Para cada item em uma lista, você deve passar uma string ou um número que identifique exclusivamente esse item entre seus irmãos. Normalmente, uma chave (key) deve vir de seus dados, como um ID de banco de dados. O React usa suas chaves para saber o que aconteceu se você mais tarde inserir, excluir ou reordenar os itens.

```js
// App.js
const products = [
  { title: "Cabbage", isFruit: false, id: 1 },
  { title: "Garlic", isFruit: false, id: 2 },
  { title: "Apple", isFruit: true, id: 3 }
];

export default function ShoppingList() {
  const listItems = products.map((product) => (
    <li
      key={product.id}
      style={{
        color: product.isFruit ? "magenta" : "darkgreen"
      }}
    >
      {product.title}
    </li>
  ));

  return <ul>{listItems}</ul>;
}
```

Para executar o projeto, use o seguinte comando. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.

```bash
npm start
```
