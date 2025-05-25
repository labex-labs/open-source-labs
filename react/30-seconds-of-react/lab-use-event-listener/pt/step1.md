# React useEventListener Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Esta função adiciona um event listener (ouvinte de evento) para o tipo de evento especificado no elemento fornecido. Para usar esta função, siga estes passos:

1.  Use o hook `useRef()` para criar uma ref que irá armazenar o `handler` (manipulador).
2.  Use o hook `useEffect()` para atualizar o valor da ref `savedHandler` sempre que o `handler` mudar.
3.  Use o hook `useEffect()` para adicionar um event listener ao elemento fornecido e limpá-lo ao desmontar.
4.  Omita o último argumento, `el`, para usar o `Window` por padrão.

Aqui está o código:

```jsx
const useEventListener = (type, handler, el = window) => {
  const savedHandler = React.useRef(handler);

  React.useEffect(() => {
    savedHandler.current = handler;
  }, [handler]);

  React.useEffect(() => {
    const listener = (e) => savedHandler.current(e);

    el.addEventListener(type, listener);

    return () => {
      el.removeEventListener(type, listener);
    };
  }, [type, el]);
};
```

E aqui está um exemplo de uso da função `useEventListener()`:

```jsx
const MyApp = () => {
  const [coords, setCoords] = React.useState({ x: 0, y: 0 });

  const updateCoords = React.useCallback(
    ({ clientX, clientY }) => {
      setCoords({ x: clientX, y: clientY });
    },
    [setCoords]
  );

  useEventListener("mousemove", updateCoords);

  return (
    <p>
      Mouse coordinates: {coords.x}, {coords.y}
    </p>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
