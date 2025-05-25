# React useAsync Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Este código cria um hook customizado que lida com chamadas assíncronas. Ele aceita uma função handler (manipuladora), `fn`, e retorna um objeto contendo as propriedades de `state` (`value`, `error` e `loading`) e uma função assíncrona `run`. A função `run` executa o callback fornecido, `fn`, enquanto usa `dispatch` para atualizar `state` conforme necessário.

```jsx
const useAsync = (fn) => {
  const initialState = { loading: false, error: null, value: null };

  const stateReducer = (state, action) => {
    switch (action.type) {
      case "start":
        return { loading: true, error: null, value: null };
      case "finish":
        return { loading: false, error: null, value: action.value };
      case "error":
        return { loading: false, error: action.error, value: null };
      default:
        return state;
    }
  };

  const [state, dispatch] = React.useReducer(stateReducer, initialState);

  const run = async (args = null) => {
    try {
      dispatch({ type: "start" });
      const value = await fn(args);
      dispatch({ type: "finish", value });
    } catch (error) {
      dispatch({ type: "error", error });
    }
  };

  return { ...state, run };
};

const RandomImage = (props) => {
  const imgFetch = useAsync((url) =>
    fetch(url).then((response) => response.json())
  );

  return (
    <div>
      <button
        onClick={() => imgFetch.run("https://dog.ceo/api/breeds/image/random")}
        disabled={imgFetch.loading}
      >
        Load image
      </button>
      <br />
      {imgFetch.loading && <div>Loading...</div>}
      {imgFetch.error && <div>Error {imgFetch.error}</div>}
      {imgFetch.value && (
        <img
          src={imgFetch.value.message}
          alt="avatar"
          width={400}
          height="auto"
        />
      )}
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<RandomImage />);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
