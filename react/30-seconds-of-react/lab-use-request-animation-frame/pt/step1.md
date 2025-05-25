# React useRequestAnimationFrame Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Para executar uma função de animação antes de cada repintura (repaint), use o hook `useRef()` para criar as variáveis `requestRef` e `previousTimeRef`. Em seguida, defina uma função `animate()` que atualiza essas variáveis, executa o `callback` e chama `Window.requestAnimationFrame()` perpetuamente. Por fim, use o hook `useEffect()` com um array vazio para inicializar o valor de `requestRef` com `Window.requestAnimationFrame()`, e use o valor retornado e `Window.cancelAnimationFrame()` para limpar quando o componente for desmontado.

Aqui está um exemplo de implementação de `useRequestAnimationFrame()`:

```jsx
const useRequestAnimationFrame = (callback) => {
  const requestRef = React.useRef();
  const previousTimeRef = React.useRef();

  const animate = (time) => {
    if (previousTimeRef.current) {
      callback(time - previousTimeRef.current);
    }
    previousTimeRef.current = time;
    requestRef.current = requestAnimationFrame(animate);
  };

  React.useEffect(() => {
    requestRef.current = requestAnimationFrame(animate);
    return () => cancelAnimationFrame(requestRef.current);
  }, []);
};
```

Para usar este hook personalizado em um componente, basta passar uma função de callback para ele. Por exemplo, para criar um contador simples que se atualiza a 100 FPS:

```jsx
const Counter = () => {
  const [count, setCount] = React.useState(0);

  useRequestAnimationFrame((deltaTime) => {
    setCount((prevCount) => (prevCount + deltaTime * 0.01) % 100);
  });

  return <p>{Math.round(count)}</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Counter />);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
