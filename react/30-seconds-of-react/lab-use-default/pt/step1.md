# React useDefault Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Aqui está o código:

```jsx
const useDefault = (defaultState, initialState) => {
  const [value, setValue] = React.useState(initialState);
  const isEmpty = value === undefined || value === null;
  return [isEmpty ? defaultState : value, setValue];
};
```

```jsx
const UserCard = () => {
  const [user, setUser] = useDefault({ name: "Adam" }, { name: "John" });

  return (
    <>
      <div>User: {user.name}</div>
      <input onChange={(e) => setUser({ name: e.target.value })} />
      <button onClick={() => setUser(null)}>Clear</button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<UserCard />);
```

Para criar um valor com estado com um _fallback_ padrão, use o _hook_ `useState()` em React. Verifique se o valor inicial é `null` ou `undefined`. Se for, retorne o `defaultState` em vez disso, caso contrário, retorne o estado `value` real e a função `setValue`. O código acima mostra como implementar essa funcionalidade em um _hook_ personalizado chamado `useDefault`.

No exemplo fornecido, `useDefault` é usado para criar um estado `user` com um valor padrão de `{ name: 'Adam' }`. O estado inicial é definido como `{ name: 'John' }`. No componente `UserCard`, `user` é exibido junto com um campo de entrada para atualizar seu nome. Um botão "Clear" também é fornecido para redefinir o estado para `null`. Finalmente, o componente é renderizado usando `ReactDOM.createRoot()`.

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
