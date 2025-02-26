# React хук useAsync

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Этот код создает пользовательский хук, который обрабатывает асинхронные вызовы. Он принимает функцию обработчика `fn` и возвращает объект, содержащий свойства `state` (`value`, `error` и `loading`), и асинхронную функцию `run`. Функция `run` запускает переданный обратный вызов `fn`, используя `dispatch` для обновления `state` по необходимости.

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
        Загрузить изображение
      </button>
      <br />
      {imgFetch.loading && <div>Загрузка...</div>}
      {imgFetch.error && <div>Ошибка {imgFetch.error}</div>}
      {imgFetch.value && (
        <img
          src={imgFetch.value.message}
          alt="аватар"
          width={400}
          height="авто"
        />
      )}
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<RandomImage />);
```

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
