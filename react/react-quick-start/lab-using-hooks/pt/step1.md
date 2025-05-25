# Usando Hooks

> O projeto React já foi fornecido na VM. Em geral, você só precisa adicionar código ao `App.js`.

Por favor, use o seguinte comando para instalar as dependências:

```bash
npm i
```

Funções que começam com `use` são chamadas de Hooks. `useState` é um Hook embutido fornecido pelo React. Você pode encontrar outros Hooks embutidos na referência da API. Você também pode escrever seus próprios Hooks combinando os existentes.

Hooks são mais restritivos do que outras funções. Você só pode chamar Hooks no topo de seus componentes (ou outros Hooks). Se você quiser usar `useState` em uma condição ou um loop, extraia um novo componente e coloque-o lá.

No exemplo anterior, cada `MyButton` tinha seu próprio `count` independente, e quando cada botão era clicado, apenas o `count` do botão clicado mudava:

![Not using hooks](../assets/1.png)

No entanto, muitas vezes você precisará que os componentes compartilhem dados e sempre atualizem juntos.

Para fazer com que ambos os componentes `MyButton` exibam o mesmo `count` e atualizem juntos, você precisa mover o estado dos botões individuais "para cima" para o componente mais próximo que os contém.

Neste exemplo, é o `MyApp`:

![Using hooks](../assets/2.png)

Agora, quando você clicar em qualquer botão, o `count` em `MyApp` mudará, o que mudará ambos os `count` em `MyButton`. Veja como você pode expressar isso em código.

Primeiro, mova o estado de `MyButton` para `MyApp`:

```js
// App.js
export default function MyApp() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <div>
      <h1>Counters that update separately</h1>
      <MyButton />
      <MyButton />
    </div>
  );
}

function MyButton() {
  // ... we're moving code from here ...
}
```

Em seguida, passe o estado de `MyApp` para cada `MyButton`, juntamente com o manipulador de clique compartilhado. Você pode passar informações para `MyButton` usando as chaves JSX, assim como você fez anteriormente com tags embutidas como `<img>`:

```js
export default function MyApp() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <div>
      <h1>Counters that update together</h1>
      <MyButton count={count} onClick={handleClick} />
      <MyButton count={count} onClick={handleClick} />
    </div>
  );
}
```

As informações que você passa dessa forma são chamadas de props. Agora, o componente `MyApp` contém o estado `count` e o manipulador de eventos `handleClick`, e passa ambos como props para cada um dos botões.

Finalmente, altere `MyButton` para ler as props que você passou de seu componente pai:

```js
function MyButton({ count, onClick }) {
  return <button onClick={onClick}>Clicked {count} times</button>;
}
```

Quando você clica no botão, o manipulador `onClick` é acionado. A prop `onClick` de cada botão foi definida para a função `handleClick` dentro de `MyApp`, então o código dentro dela é executado. Esse código chama `setCount(count + 1)`, incrementando a variável de estado `count`. O novo valor de `count` é passado como uma prop para cada botão, então todos eles mostram o novo valor. Isso é chamado de "elevar o estado" ("lifting state up"). Ao mover o estado para cima, você o compartilhou entre os componentes.

```js
import { useState } from "react";

export default function MyApp() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <div>
      <h1>Counters that update together</h1>
      <MyButton count={count} onClick={handleClick} />
      <MyButton count={count} onClick={handleClick} />
    </div>
  );
}

function MyButton({ count, onClick }) {
  return <button onClick={onClick}>Clicked {count} times</button>;
}
```

Para executar o projeto, use o seguinte comando. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.

```bash
npm start
```
