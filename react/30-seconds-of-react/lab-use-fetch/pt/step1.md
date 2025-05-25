# React useFetch Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Aqui está o código:

```jsx
const useFetch = (url, options) => {
  const [response, setResponse] = React.useState(null);
  const [error, setError] = React.useState(null);
  const [abort, setAbort] = React.useState(() => {});

  React.useEffect(() => {
    const abortController = new AbortController();
    const signal = abortController.signal;

    const fetchData = async () => {
      try {
        const res = await fetch(url, { ...options, signal });
        const json = await res.json();
        setResponse(json);
      } catch (error) {
        setError(error);
      }
    };
    fetchData();

    return () => {
      abort();
    };
  }, []);

  return { response, error, abort };
};

const ImageFetch = (props) => {
  const res = useFetch("https://dog.ceo/api/breeds/image/random", {});

  if (!res.response) {
    return <div>Loading...</div>;
  }

  const imageUrl = res.response.message;

  return (
    <div>
      <img src={imageUrl} alt="avatar" width={400} height="auto" />
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<ImageFetch />);
```

Explicação:

- O objetivo do código é implementar uma chamada `fetch()` de forma declarativa usando hooks do React.
- O hook `useFetch` recebe dois parâmetros: uma `url` e um objeto `options`.
- O hook inicializa três variáveis de estado usando o hook `useState()`: `response`, `error` e `abort`.
- O hook `useEffect()` é usado para chamar assincronamente `fetch()` e atualizar as variáveis de estado de acordo.
- Um `AbortController` é usado para permitir o cancelamento da requisição, e é usado para cancelar a requisição quando o componente é desmontado.
- O hook retorna um objeto contendo as variáveis de estado `response`, `error` e `abort`.
- O componente `ImageFetch` usa o hook `useFetch` para obter uma imagem aleatória de um cachorro e exibi-la em um elemento `<img>`.

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
