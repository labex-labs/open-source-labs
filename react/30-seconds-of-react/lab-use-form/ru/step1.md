# Хук useForm в React

> В ВМ уже предоставлены `index.html` и `script.js`. В общем случае вам нужно только добавлять код в `script.js` и `style.css`.

Для создания состояния на основе полей формы вы можете использовать хук `useState()`, чтобы создать переменную состояния для значений в форме. Затем создайте функцию, которая обновляет переменную состояния в зависимости от соответствующего события, которое срабатывает при взаимодействии с полем формы.

Вот пример реализации:

```jsx
const useForm = (initialValues) => {
  const [values, setValues] = React.useState(initialValues);

  return [
    values,
    (e) => {
      setValues({
        ...values,
        [e.target.name]: e.target.value
      });
    }
  ];
};
```

В приведенном выше примере `useForm()` принимает начальный объект состояния, создает переменную состояния `values` с использованием `useState()` и возвращает массив, содержащий `values` и функцию, которая обновляет `values` в зависимости от переданного ей события.

Вы можете использовать `useForm()` в компоненте формы следующим образом:

```jsx
const Form = () => {
  const initialState = { email: "", password: "" };
  const [values, setValues] = useForm(initialState);

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(values);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="email" name="email" onChange={setValues} />
      <input type="password" name="password" onChange={setValues} />
      <button type="submit">Submit</button>
    </form>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Form />);
```

В компоненте `Form` функция `useForm()` вызывается с начальным объектом состояния и возвращает массив, содержащий `values` и `setValues()`. Функция `handleSubmit()` выводит объект `values` в консоль при отправке формы. Элементы `input` настроены для обновления значений формы с использованием функции `setValues()`.

Пожалуйста, нажмите кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
