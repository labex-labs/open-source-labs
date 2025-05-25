# Alerta Fechável

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Renderiza um componente de alerta com a prop `type`.

O componente `Alert` recebe as seguintes props:

- `isDefaultShown`: um booleano que determina se o alerta é exibido inicialmente ou não (o padrão é `false`)
- `timeout`: um número que especifica a duração em milissegundos antes que o alerta desapareça (o padrão é `250`)
- `type`: uma string que determina o tipo de alerta (por exemplo, "warning", "error", "info")
- `message`: uma string que contém a mensagem a ser exibida no alerta

O componente faz o seguinte:

- Usa o hook `useState()` para criar as variáveis de estado `isShown` e `isLeaving` e define ambas inicialmente como `false`.
- Define uma variável `timeoutId` para manter a instância do timer para limpar no unmount do componente.
- Usa o hook `useEffect()` para atualizar o valor de `isShown` para `true` e limpar o intervalo usando `timeoutId` quando o componente é desmontado.
- Define uma função `closeAlert` para definir o componente como removido do DOM, exibindo uma animação de desaparecimento e definindo `isShown` como `false` via `setTimeout()`.
- Renderiza o componente de alerta se `isShown` for `true`. O componente tem os estilos apropriados com base na prop `type` e desaparece se `isLeaving` for `true`.

Aqui está o código:

```css
@keyframes leave {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}

.alert {
  padding: 0.75rem 0.5rem;
  margin-bottom: 0.5rem;
  text-align: left;
  padding-right: 40px;
  border-radius: 4px;
  font-size: 16px;
  position: relative;
}

.alert.warning {
  color: #856404;
  background-color: #fff3cd;
  border-color: #ffeeba;
}

.alert.error {
  color: #721c24;
  background-color: #f8d7da;
  border-color: #f5c6cb;
}

.alert.leaving {
  animation: leave 0.5s forwards;
}

.alert .close {
  position: absolute;
  top: 0;
  right: 0;
  padding: 0 0.75rem;
  color: #333;
  border: 0;
  height: 100%;
  cursor: pointer;
  background: none;
  font-weight: 600;
  font-size: 16px;
}

.alert .close::after {
  content: "x";
}
```

```jsx
const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
  const [isShown, setIsShown] = React.useState(isDefaultShown);
  const [isLeaving, setIsLeaving] = React.useState(false);

  let timeoutId = null;

  React.useEffect(() => {
    setIsShown(true);
    return () => {
      clearTimeout(timeoutId);
    };
  }, [isDefaultShown, timeout, timeoutId]);

  const closeAlert = () => {
    setIsLeaving(true);
    timeoutId = setTimeout(() => {
      setIsLeaving(false);
      setIsShown(false);
    }, timeout);
  };

  return (
    isShown && (
      <div
        className={`alert ${type} ${isLeaving ? "leaving" : ""}`}
        role="alert"
      >
        <button className="close" onClick={closeAlert} />
        {message}
      </div>
    )
  );
};
```

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Alert type="info" message="This is info" />
);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
