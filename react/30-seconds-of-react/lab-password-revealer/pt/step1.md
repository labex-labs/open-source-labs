# Alternância Mostrar/Ocultar Senha

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

O código a seguir renderiza um campo de entrada de senha com um botão de revelação. Ele usa o hook `useState()` para criar a variável de estado `shown` e definir seu valor inicial como `false`. Quando o botão "Mostrar/Ocultar" é clicado, a função `setShown` é chamada, alternando o `type` da entrada entre `'text'` e `'password'`.

```jsx
const PasswordRevealer = ({ value }) => {
  const [shown, setShown] = React.useState(false);
  return (
    <>
      <input type={shown ? "text" : "password"} value={value} />
      <button onClick={() => setShown(!shown)}>Show/Hide</button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <PasswordRevealer />
);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
