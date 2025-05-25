# React useGetSet Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Este trecho de código define um hook React personalizado chamado `useGetSet` que cria um valor com estado e retorna um par de funções para obter e definir seu valor. O componente `Counter` usa este hook para implementar um incremento atrasado de uma contagem exibida em um botão.

```jsx
const useGetSet = (initialState) => {
  const stateRef = React.useRef(initialState);
  const [, update] = React.useReducer(() => ({}), {});

  const getState = React.useCallback(() => stateRef.current, []);
  const setState = React.useCallback((newState) => {
    stateRef.current = newState;
    update();
  }, []);

  return [getState, setState];
};

const Counter = () => {
  const [getCount, setCount] = useGetSet(0);
  const onClick = React.useCallback(() => {
    setTimeout(() => {
      setCount(getCount() + 1);
    }, 1000);
  }, [getCount, setCount]);

  return <button onClick={onClick}>Count: {getCount()}</button>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Counter />);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
