# Atualizando a Tela

> O projeto React já foi fornecido na VM. Em geral, você só precisa adicionar código ao `App.js`.

Por favor, use o seguinte comando para instalar as dependências:

```bash
npm i
```

Frequentemente, você vai querer que seu componente "lembre" de alguma informação e a exiba. Por exemplo, talvez você queira contar o número de vezes que um botão é clicado. Para fazer isso, adicione estado ao seu componente.

Primeiro, importe `useState` do React:

```js
import { useState } from "react";
```

Agora você pode declarar uma variável de estado dentro do seu componente:

```js
function MyButton() {
  const [count, setCount] = useState(0);
  // ...
```

Você obterá duas coisas de `useState`: o estado atual (`count`) e a função que permite atualizá-lo (`setCount`). Você pode dar a eles qualquer nome, mas a convenção é escrever `[algo, setAlgo]`.

Na primeira vez que o botão é exibido, `count` será `0` porque você passou 0 para `useState()`. Quando você quiser mudar o estado, chame `setCount()` e passe o novo valor para ele. Clicar neste botão incrementará o contador:

```js
function MyButton() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return <button onClick={handleClick}>Clicked {count} times</button>;
}
```

React chamará sua função de componente novamente. Desta vez, `count` será `1`. Então será `2`. E assim por diante.

Se você renderizar o mesmo componente várias vezes, cada um terá seu próprio estado. Clique em cada botão separadamente:

```js
// App.js
import { useState } from "react";

export default function MyApp() {
  return (
    <div>
      <h1>Counters that update separately</h1>
      <MyButton />
      <MyButton />
    </div>
  );
}

function MyButton() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return <button onClick={handleClick}>Clicked {count} times</button>;
}
```

Observe como cada botão "lembra" seu próprio estado `count` e não afeta outros botões.

Para executar o projeto, use o seguinte comando. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.

```bash
npm start
```
