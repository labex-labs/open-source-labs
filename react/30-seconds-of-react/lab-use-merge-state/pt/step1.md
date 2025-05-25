# React useMergeState Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Para criar um valor com estado e uma função para atualizá-lo mesclando o novo estado fornecido, use o hook `useState()` para criar uma variável de estado e inicializá-la com `initialState`. Crie uma função que atualizará a variável de estado mesclando o novo estado fornecido com o existente. Se o novo estado for uma função, chame-a com o estado anterior como argumento e use o resultado. Se nenhum argumento for fornecido, a variável de estado será inicializada com um objeto vazio (`{}`). O código a seguir demonstra como implementar isso usando o custom hook `useMergeState`:

```jsx
const useMergeState = (initialState = {}) => {
  const [value, setValue] = React.useState(initialState);

  const mergeState = (newState) => {
    if (typeof newState === "function") {
      newState = newState(value);
    }
    setValue({ ...value, ...newState });
  };

  return [value, mergeState];
};
```

Aqui está um exemplo de uso do hook `useMergeState` em um componente chamado `MyApp`:

```jsx
const MyApp = () => {
  const [data, setData] = useMergeState({ name: "John", age: 20 });

  return (
    <>
      <input
        value={data.name}
        onChange={(e) => setData({ name: e.target.value })}
      />
      <button onClick={() => setData(({ age }) => ({ age: age - 1 }))}>
        -
      </button>
      {data.age}
      <button onClick={() => setData(({ age }) => ({ age: age + 1 }))}>
        +
      </button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
