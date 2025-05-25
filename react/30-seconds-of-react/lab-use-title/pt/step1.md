# React useTitle Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Para definir o título da página, você pode usar o custom hook `useTitle`. Este hook usa `typeof` para verificar se o `Document` está definido. Se estiver definido, o hook `useRef()` é usado para armazenar o título original do `Document`. O hook `useEffect()` é então usado para definir `Document.title` para o valor passado quando o componente monta e para limpar quando desmonta.

```jsx
const useTitle = (title) => {
  const documentDefined = typeof document !== "undefined";
  const originalTitle = React.useRef(documentDefined ? document.title : null);

  React.useEffect(() => {
    if (!documentDefined) return;

    if (document.title !== title) {
      document.title = title;
    }

    return () => {
      document.title = originalTitle.current;
    };
  }, [title]);
};
```

No código de exemplo, o componente `Alert` usa o hook `useTitle` para definir o título como "Alert". O componente `MyApp` renderiza um botão que alterna o componente `Alert`.

```jsx
const Alert = () => {
  useTitle("Alert");

  return (
    <div>
      <p>Alert! Title has changed</p>
    </div>
  );
};

const MyApp = () => {
  const [alertOpen, setAlertOpen] = React.useState(false);

  return (
    <div>
      <button onClick={() => setAlertOpen(!alertOpen)}>Toggle alert</button>
      {alertOpen && <Alert />}
    </div>
  );
};

ReactDOM.render(<MyApp />, document.getElementById("root"));
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
