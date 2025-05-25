# React useTimeout Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Para implementar `setTimeout()` de forma declarativa, crie um custom hook que recebe um `callback` e um `delay`. Use o hook `useRef()` para criar uma `ref` para a função de callback e use o hook `useEffect()` para lembrar o último callback. Em seguida, use o hook `useEffect()` para configurar o timeout e limpá-lo.

Aqui está um trecho de código de exemplo que demonstra essa abordagem:

```jsx
const useTimeout = (callback, delay) => {
  const savedCallback = React.useRef();

  React.useEffect(() => {
    savedCallback.current = callback;
  }, [callback]);

  React.useEffect(() => {
    const tick = () => {
      savedCallback.current();
    };
    if (delay !== null) {
      let id = setTimeout(tick, delay);
      return () => clearTimeout(id);
    }
  }, [delay]);
};

const OneSecondTimer = (props) => {
  const [seconds, setSeconds] = React.useState(0);

  useTimeout(() => {
    setSeconds(seconds + 1);
  }, 1000);

  return <p>{seconds}</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<OneSecondTimer />);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
