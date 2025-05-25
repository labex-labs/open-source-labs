# React useNavigatorOnLine Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Para verificar se o cliente está online ou offline, você pode criar uma função `getOnLineStatus` que utiliza a API web `Navigator.onLine`. Em seguida, para implementar essa funcionalidade em um componente React, você pode usar o hook customizado `useNavigatorOnLine`. Este hook cria uma variável de estado chamada `status` usando o hook `useState()` e a define para o valor retornado por `getOnLineStatus()`. O hook `useEffect()` é usado para adicionar listeners de eventos para quando o status online/offline muda, atualizar a variável de estado `status` de acordo e limpar esses listeners quando o componente desmonta. Finalmente, a variável `isOnline` retornada por `useNavigatorOnLine()` pode ser usada para renderizar uma mensagem indicando se o cliente está online ou offline.

```jsx
const getOnLineStatus = () =>
  typeof navigator !== "undefined" && typeof navigator.onLine === "boolean"
    ? navigator.onLine
    : true;

const useNavigatorOnLine = () => {
  const [status, setStatus] = React.useState(getOnLineStatus());

  const setOnline = () => setStatus(true);
  const setOffline = () => setStatus(false);

  React.useEffect(() => {
    window.addEventListener("online", setOnline);
    window.addEventListener("offline", setOffline);

    return () => {
      window.removeEventListener("online", setOnline);
      window.removeEventListener("offline", setOffline);
    };
  }, []);

  return status;
};

const StatusIndicator = () => {
  const isOnline = useNavigatorOnLine();

  return <span>You are {isOnline ? "online" : "offline"}.</span>;
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <StatusIndicator />
);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
