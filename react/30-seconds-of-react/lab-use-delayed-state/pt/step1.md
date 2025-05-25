# React useDelayedState Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Para atrasar a criação de um valor com estado até que uma condição seja atendida, siga estes passos:

1. Use o hook `useState()` para criar um valor com estado contendo o `state` real e um booleano, `loaded`.
2. Use o hook `useEffect()` para atualizar o valor com estado se a `condition` ou `loaded` mudar.
3. Crie uma função, `updateState`, que só atualiza o valor `state` se `loaded` for verdadeiro (truthy).

```jsx
const useDelayedState = (initialState, condition) => {
  const [{ state, loaded }, setState] = React.useState({
    state: null,
    loaded: false
  });

  React.useEffect(() => {
    if (!loaded && condition) setState({ state: initialState, loaded: true });
  }, [condition, loaded]);

  const updateState = (newState) => {
    if (!loaded) return;
    setState({ state: newState, loaded });
  };

  return [state, updateState];
};
```

Aqui está um exemplo de como usar o hook `useDelayedState`:

```jsx
const App = () => {
  const [branches, setBranches] = React.useState([]);
  const [selectedBranch, setSelectedBranch] = useDelayedState(
    branches[0],
    branches.length
  );

  React.useEffect(() => {
    const handle = setTimeout(() => {
      setBranches(["master", "staging", "test", "dev"]);
    }, 2000);
    return () => {
      handle && clearTimeout(handle);
    };
  }, []);

  return (
    <div>
      <p>Selected branch: {selectedBranch}</p>
      <select onChange={(e) => setSelectedBranch(e.target.value)}>
        {branches.map((branch) => (
          <option key={branch} value={branch}>
            {branch}
          </option>
        ))}
      </select>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
