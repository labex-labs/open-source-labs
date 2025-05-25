# Respondendo a Eventos

> O projeto React já foi fornecido na VM. Em geral, você só precisa adicionar código ao `App.js`.

Por favor, use o seguinte comando para instalar as dependências:

```bash
npm i
```

O React permite que você adicione manipuladores de eventos ao seu JSX. Manipuladores de eventos são suas próprias funções que serão acionadas em resposta a interações como clicar, passar o mouse, focar em entradas de formulário e assim por diante.

Para adicionar um manipulador de eventos, você primeiro definirá uma função e, em seguida, [passará-a como uma prop](https://react.dev/learn/passing-props-to-a-component) para a tag JSX apropriada. Por exemplo, aqui está um botão que ainda não faz nada:

```js
// App.js
export default function Button() {
  return <button>I don't do anything</button>;
}
```

Você pode fazê-lo mostrar uma mensagem quando um usuário clica, seguindo estas três etapas:

1. Declare uma função chamada `handleClick` dentro do seu componente `Button`.
2. Implemente a lógica dentro dessa função (use `alert` para mostrar a mensagem).
3. Adicione `onClick={handleClick}` ao JSX `<button>`.

```js
export default function Button() {
  function handleClick() {
    alert("You clicked me!");
  }

  return <button onClick={handleClick}>Click me</button>;
}
```

Você definiu a função handleClick e, em seguida, passou-a como uma prop para `<button>`. handleClick é um manipulador de eventos. Funções de manipulador de eventos:

- Geralmente são definidas dentro de seus componentes.
- Têm nomes que começam com handle, seguido pelo nome do evento.

Para executar o projeto, use o seguinte comando. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.

```bash
npm start
```

Por convenção, é comum nomear manipuladores de eventos como handle seguido pelo nome do evento. Você frequentemente verá `onClick={handleClick}`, `onMouseEnter={handleMouseEnter}`, e assim por diante.

Alternativamente, você pode definir um manipulador de eventos inline no JSX:

```js
<button onClick={function handleClick() {
  alert('You clicked me!');
}}>
```

Ou, de forma mais concisa, usando uma função de seta:

```js
<button onClick={() => {
  alert('You clicked me!');
}}>
```

Todos esses estilos são equivalentes. Manipuladores de eventos inline são convenientes para funções curtas.
