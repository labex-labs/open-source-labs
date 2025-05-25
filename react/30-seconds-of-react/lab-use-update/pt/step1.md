# React useUpdate Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Para forçar um componente a re-renderizar quando chamado, use o hook `useReducer()` para criar um novo objeto toda vez que ele for atualizado e retorne seu dispatch. Aqui está um exemplo de implementação da função `useUpdate()`:

```jsx
const useUpdate = () => {
  const [, update] = React.useReducer(() => ({}));
  return update;
};
```

Você pode então usar `useUpdate()` em seu componente para acionar um re-render quando necessário:

```jsx
const MyApp = () => {
  const update = useUpdate();

  return (
    <>
      <div>Time: {Date.now()}</div>
      <button onClick={update}>Update</button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
