# Хуки useFetch в React

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Вот код:

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

Пояснение:

- Целью кода является реализация вызова `fetch()` в декларативном стиле с использованием хуков React.
- Хуки `useFetch` принимает два параметра: `url` и объект `options`.
- Хуки инициализирует три переменные состояния с использованием хуков `useState()`: `response`, `error` и `abort`.
- Хуки `useEffect()` используется для асинхронного вызова `fetch()` и соответствующего обновления переменных состояния.
- `AbortController` используется для возможности отмены запроса, и он используется для отмены запроса при размонтировании компонента.
- Хуки возвращает объект, содержащий переменные состояния `response`, `error` и `abort`.
- Компонент `ImageFetch` использует хуки `useFetch` для получения случайной картинки собаки и отображения ее в элементе `<img>`.

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
