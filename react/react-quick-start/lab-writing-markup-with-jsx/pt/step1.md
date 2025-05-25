# Escrevendo Marcação com JSX

> O projeto React já foi fornecido na VM. Em geral, você só precisa adicionar código ao `App.js`.

Por favor, use o seguinte comando para instalar as dependências:

```bash
npm i
```

A sintaxe de marcação que você viu acima é chamada JSX. É opcional, mas a maioria dos projetos React usa JSX por sua conveniência.

JSX é mais rigoroso que HTML. Você precisa fechar tags como `<br />`. Seu componente também não pode retornar múltiplas tags JSX. Você precisa envolvê-las em um pai compartilhado, como um `<h1>...</h1>` ou um wrapper vazio `<>...</>`:

```js
// App.js
export default function Profile() {
  return (
    <>
      <h1>Hedy Lamarr</h1>
    </>
  );
}
```

Se você tiver muito HTML para converter para JSX, pode usar um [conversor online](https://transform.tools/html-to-jsx).

Para executar o projeto, use o seguinte comando. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.

```bash
npm start
```
