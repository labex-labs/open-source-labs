# Hook React useKeyPress

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Esta função monitora as mudanças no estado pressionado de uma determinada tecla. Para usá-la:

- Chame `useKeyPress()` com a tecla alvo como argumento.
- `useKeyPress()` retorna um valor booleano que indica se a tecla está atualmente pressionada.
- A função usa o hook `useState()` para criar uma variável de estado que armazena o estado pressionado da tecla fornecida.
- Ela define duas funções de tratamento (handler) que atualizam a variável de estado em key down ou key up, respectivamente.
- O hook `useEffect()` e `EventTarget.addEventListener()` são usados para lidar com os eventos `'keydown'` e `'keyup'`.
- Finalmente, `EventTarget.removeEventListener()` é usado para realizar a limpeza após o componente ser desmontado.

```jsx
const useKeyPress = (targetKey) => {
  const [isKeyPressed, setKeyPressed] = React.useState(false);

  const handleKeyDown = ({ key }) => {
    if (key === targetKey) setKeyPressed(true);
  };

  const handleKeyUp = ({ key }) => {
    if (key === targetKey) setKeyPressed(false);
  };

  React.useEffect(() => {
    window.addEventListener("keydown", handleKeyDown);
    window.addEventListener("keyup", handleKeyUp);

    return () => {
      window.removeEventListener("keydown", handleKeyDown);
      window.removeEventListener("keyup", handleKeyUp);
    };
  }, [targetKey]);

  return isKeyPressed;
};
```

Aqui está um exemplo de uso de `useKeyPress()` em um componente React:

```jsx
const MyApp = () => {
  const isWKeyPressed = useKeyPress("w");

  return <p>The "w" key is {!isWKeyPressed ? "not " : ""}pressed!</p>;
};

ReactDOM.render(<MyApp />, document.getElementById("root"));
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
