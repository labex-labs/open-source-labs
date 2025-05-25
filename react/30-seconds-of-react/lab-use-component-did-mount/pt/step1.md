# React useComponentDidMount Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Para executar uma função de callback imediatamente após um componente ser montado, você pode usar o hook `useEffect()` com um array vazio como o segundo argumento. Isso garantirá que o callback fornecido seja executado apenas uma vez quando o componente for montado. A função `useComponentDidMount()` mostrada abaixo usa este hook para implementar o mesmo comportamento do método de ciclo de vida `componentDidMount()` dos componentes de classe.

```jsx
const useComponentDidMount = (onMountHandler) => {
  React.useEffect(() => {
    onMountHandler();
  }, []);
};

const Mounter = () => {
  useComponentDidMount(() => console.log("Component did mount"));

  return <div>Check the console!</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Mounter />);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
