# Hook `useSet` do React

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Esta função cria um objeto `Set` com estado e um conjunto de funções que podem manipular o estado.

Para usar esta função:

- Chame `useState()` e o construtor `Set` para criar um novo `Set` a partir do `initialValue`.
- Use `useMemo()` para criar um conjunto de funções não mutáveis que podem manipular a variável de estado `set`. Use o setter de estado para criar um novo `Set` sempre.
- Retorne tanto a variável de estado `set` quanto as `actions` criadas.

Aqui está um exemplo de implementação desta função:

```jsx
const useSet = (initialValue) => {
  const [set, setSet] = React.useState(new Set(initialValue));

  const actions = React.useMemo(
    () => ({
      add: (item) => setSet((prevSet) => new Set([...prevSet, item])),
      remove: (item) =>
        setSet((prevSet) => new Set([...prevSet].filter((i) => i !== item))),
      clear: () => setSet(new Set())
    }),
    [setSet]
  );

  return [set, actions];
};
```

Aqui está um exemplo de uso desta função:

```jsx
const MyApp = () => {
  const [set, { add, remove, clear }] = useSet(new Set(["apples"]));

  return (
    <div>
      <button onClick={() => add(String(Date.now()))}>Add</button>
      <button onClick={() => clear()}>Reset</button>
      <button onClick={() => remove("apples")} disabled={!set.has("apples")}>
        Remove apples
      </button>
      <pre>{JSON.stringify([...set], null, 2)}</pre>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
