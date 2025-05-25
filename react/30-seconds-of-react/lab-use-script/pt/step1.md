# React useScript Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Para carregar dinamicamente um script externo, use o hook `useState()` para criar uma variável de estado que armazena o status de carregamento do script. Em seguida, use o hook `useEffect()` para lidar com toda a lógica de carregamento e descarregamento do script sempre que o `src` mudar. Se nenhum valor `src` estiver presente, defina o `status` como `'idle'` e retorne. Use `Document.querySelector()` para verificar se um elemento `<script>` com o valor `src` apropriado existe. Se nenhum elemento relevante existir, use `Document.createElement()` para criar um e dar a ele os atributos apropriados. Use o atributo `data-status` como uma forma de indicar o status do script, definindo-o inicialmente como `'loading'`. Se um elemento relevante existir, ignore a inicialização e atualize o `status` a partir de seu atributo `data-status`. Isso garante que nenhum elemento duplicado seja criado. Use `EventTarget.addEventListener()` para ouvir os eventos `'load'` e `'error'` e tratá-los atualizando o atributo `data-status` e a variável de estado `status`. Finalmente, quando o componente for desmontado, use `Document.removeEventListener()` para remover quaisquer listeners vinculados ao elemento.

Aqui está uma implementação de exemplo do hook `useScript`:

```jsx
const useScript = (src) => {
  const [status, setStatus] = React.useState(src ? "loading" : "idle");

  React.useEffect(() => {
    if (!src) {
      setStatus("idle");
      return;
    }

    let script = document.querySelector(`script[src="${src}"]`);

    if (!script) {
      script = document.createElement("script");
      script.src = src;
      script.async = true;
      script.setAttribute("data-status", "loading");
      document.body.appendChild(script);

      const setDataStatus = (event) => {
        script.setAttribute(
          "data-status",
          event.type === "load" ? "ready" : "error"
        );
      };
      script.addEventListener("load", setDataStatus);
      script.addEventListener("error", setDataStatus);
    } else {
      setStatus(script.getAttribute("data-status"));
    }

    const setStateStatus = (event) => {
      setStatus(event.type === "load" ? "ready" : "error");
    };

    script.addEventListener("load", setStateStatus);
    script.addEventListener("error", setStateStatus);

    return () => {
      if (script) {
        script.removeEventListener("load", setStateStatus);
        script.removeEventListener("error", setStateStatus);
      }
    };
  }, [src]);

  return status;
};
```

Aqui está um exemplo de uso do hook `useScript`:

```jsx
const script =
  "data:text/plain;charset=utf-8;base64,KGZ1bmN0aW9uKCl7IGNvbnNvbGUubG9nKCdIZWxsbycpIH0pKCk7";

const Child = () => {
  const status = useScript(script);
  return <p>Child status: {status}</p>;
};

const MyApp = () => {
  const status = useScript(script);
  return (
    <>
      <p>Parent status: {status}</p>
      <Child />
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
