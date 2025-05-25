# React useComponentWillUnmount Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Para executar um callback imediatamente antes que um componente seja desmontado e destruído, você pode usar o hook `useEffect()` com um array vazio como o segundo argumento. Retorne o callback fornecido para ser executado apenas uma vez antes da limpeza. Este comportamento é semelhante ao método de ciclo de vida `componentWillUnmount()` dos componentes de classe. Você também pode usar o seguinte trecho de código para criar um hook personalizado `useComponentWillUnmount()` que recebe uma função `onUnmountHandler` como argumento e a executa antes que o componente seja desmontado:

```jsx
const useComponentWillUnmount = (onUnmountHandler) => {
  React.useEffect(
    () => () => {
      onUnmountHandler();
    },
    []
  );
};
```

Você pode então usar este hook personalizado em seu componente funcional da seguinte forma:

```jsx
const Unmounter = () => {
  useComponentWillUnmount(() => console.log("Component will unmount"));

  return <div>Check the console!</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Unmounter />);
```

Isso registrará "Component will unmount" no console quando o componente estiver prestes a ser desmontado.

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
