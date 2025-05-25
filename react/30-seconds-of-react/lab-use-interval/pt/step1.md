# React useInterval Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Para implementar `setInterval()` de maneira declarativa, você pode criar um hook customizado que recebe um `callback` e um `delay`. O primeiro passo é usar o hook `useRef()` para criar uma `ref` para a função de callback. Em seguida, use um hook `useEffect()` para lembrar o último `callback` sempre que ele mudar. Finalmente, use um hook `useEffect()` dependente de `delay` para configurar o intervalo e limpar.

Aqui está um trecho de código de exemplo para o hook customizado:

```jsx
const useInterval = (callback, delay) => {
  const savedCallback = React.useRef();

  React.useEffect(() => {
    savedCallback.current = callback;
  }, [callback]);

  React.useEffect(() => {
    const tick = () => {
      savedCallback.current();
    };
    if (delay !== null) {
      let id = setInterval(tick, delay);
      return () => clearInterval(id);
    }
  }, [delay]);
};
```

Você pode então usar este hook customizado em seus componentes. Por exemplo, para criar um timer que atualiza a cada segundo:

```jsx
const Timer = (props) => {
  const [seconds, setSeconds] = React.useState(0);

  useInterval(() => {
    setSeconds(seconds + 1);
  }, 1000);

  return <p>{seconds}</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Timer />);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
