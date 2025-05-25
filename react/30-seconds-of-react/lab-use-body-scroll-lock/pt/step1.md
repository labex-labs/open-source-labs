# React useBodyScrollLock Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Este trecho de código permite que os usuários bloqueiem a rolagem do `body` quando um modal está aberto. Veja como funciona:

Primeiro, a função `useBodyScrollLock` é definida, que usa o hook `useLayoutEffect` para bloquear a rolagem do elemento `body`. Este hook é executado apenas uma vez quando o componente é montado, e ele define o valor `overflow` do elemento `body` para `'hidden'`. Quando o componente é desmontado, o valor original de `overflow` é restaurado.

```jsx
const useBodyScrollLock = () => {
  React.useLayoutEffect(() => {
    const originalStyle = window.getComputedStyle(document.body).overflow;
    document.body.style.overflow = "hidden";
    return () => (document.body.style.overflow = originalStyle);
  }, []);
};
```

Em seguida, o componente `Modal` é definido, que utiliza a função `useBodyScrollLock`. Este componente exibe uma mensagem em uma caixa que é centralizada na tela. Quando a caixa é clicada, o modal é fechado e a rolagem do `body` é desbloqueada.

```jsx
const Modal = ({ onClose }) => {
  useBodyScrollLock();

  return (
    <div
      style={{
        zIndex: 100,
        background: "rgba(0,0,0,0.25)",
        display: "flex",
        justifyContent: "center",
        alignItems: "center"
      }}
      onClick={onClose}
    >
      <p style={{ padding: 8, borderRadius: 8, background: "#fff" }}>
        Scroll locked! <br /> Click me to unlock
      </p>
    </div>
  );
};
```

Finalmente, o componente `MyApp` é definido, que renderiza um botão que abre o componente `Modal` quando clicado.

```jsx
const MyApp = () => {
  const [modalOpen, setModalOpen] = React.useState(false);

  return (
    <div
      style={{
        height: "400vh",
        textAlign: "center",
        paddingTop: 100,
        background: "linear-gradient(to bottom, #1fa2ff, #12d8fa, #a6ffcb)"
      }}
    >
      <button onClick={() => setModalOpen(true)}>Open modal</button>
      {modalOpen && <Modal onClose={() => setModalOpen(false)} />}
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
