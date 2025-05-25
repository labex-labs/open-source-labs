# Renderização Condicional

> O projeto React já foi fornecido na VM. Em geral, você só precisa adicionar código ao `App.js`.

Por favor, use o seguinte comando para instalar as dependências:

```bash
npm i
```

No React, não há sintaxe especial para escrever condições. Em vez disso, você usará as mesmas técnicas que usa ao escrever código JavaScript regular. Por exemplo, você pode usar uma instrução `if` para incluir condicionalmente JSX:

```js
if (isPacked) {
  return <li className="item">{name} ✔</li>;
}
return <li className="item">{name}</li>;
```

Se você preferir um código mais compacto, pode usar o operador condicional `?`. Ao contrário de `if`, ele funciona dentro do JSX:

```js
return <li className="item">{isPacked ? name + " ✔" : name}</li>;
```

Quando você não precisa do ramo `else`, você também pode usar uma sintaxe `&&` lógica mais curta:

```js
return <li className="item">{isPacked && name + " ✔"}</li>;
```

Se a prop `isPacked` for verdadeira, este código retorna uma árvore JSX diferente. Com esta alteração, alguns dos itens recebem uma marca de verificação no final:

```js
// App.js
function Item({ name, isPacked }) {
  if (isPacked) {
    return <li className="item">{name} ✔</li>;
  }
  return <li className="item">{name}</li>;
}

export default function PackingList() {
  return (
    <section>
      <h1>Sally Ride's Packing List</h1>
      <ul>
        <Item isPacked={true} name="Space suit" />
        <Item isPacked={true} name="Helmet with a golden leaf" />
        <Item isPacked={false} name="Photo of Tam" />
      </ul>
    </section>
  );
}
```

Para executar o projeto, use o seguinte comando. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.

```bash
npm start
```
