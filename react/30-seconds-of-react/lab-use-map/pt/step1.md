# React useMap Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

- O hook `useMap()` cria um objeto `Map` com estado e um conjunto de funções para manipulá-lo usando hooks React.
- O hook `useState()` inicializa o estado `Map` com o `initialValue`.
- O hook `useMemo()` cria um conjunto de ações não mutáveis que manipulam a variável de estado `map` usando o setter de estado para criar um novo `Map` a cada vez.
- O hook `useMap()` retorna um array contendo a variável de estado `map` e as `actions` criadas.
- O componente `MyApp` usa o hook `useMap()` para inicializar o objeto `Map` com estado e fornece botões para adicionar, resetar e remover itens do `Map`.
- A função `JSON.stringify()` formata o objeto `Map` em uma string JSON legível.

```jsx
const useMap = (initialValue) => {
  const [map, setMap] = React.useState(new Map(initialValue));

  const actions = React.useMemo(
    () => ({
      set: (key, value) =>
        setMap((prevMap) => {
          const nextMap = new Map(prevMap);
          nextMap.set(key, value);
          return nextMap;
        }),
      remove: (key) =>
        setMap((prevMap) => {
          const nextMap = new Map(prevMap);
          nextMap.delete(key);
          return nextMap;
        }),
      clear: () => setMap(new Map())
    }),
    [setMap]
  );

  return [map, actions];
};

const MyApp = () => {
  const [map, { set, remove, clear }] = useMap([["apples", 10]]);

  const handleAdd = () => set(Date.now(), new Date().toJSON());
  const handleReset = () => clear();
  const handleRemove = () => remove("apples");

  return (
    <div>
      <button onClick={handleAdd}>Add</button>
      <button onClick={handleReset}>Reset</button>
      <button onClick={handleRemove} disabled={!map.has("apples")}>
        Remove apples
      </button>
      <pre>{JSON.stringify(Object.fromEntries(map), null, 2)}</pre>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
