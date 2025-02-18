# Ссылка для отправки электронной почты

> Файлы `index.html` и `script.js` уже предоставлены в виртуальной машине (VM). Как правило, вам нужно добавить код только в файлы `script.js` и `style.css`.

Эта функция создает ссылку, при нажатии на которую открывается почтовый клиент пользователя и заполняется новое письмо с указанной темой и текстом. Ссылка форматируется с использованием протокола `mailto:`.

Для использования функции укажите пропс (prop) `email` с адресом электронной почты получателя и, по желанию, укажите пропсы `subject` и `body` для заполнения письма начальным содержимым. Эти пропсы безопасно кодируются с использованием `encodeURIComponent` перед добавлением в URL ссылки.

Ссылка отображается с предоставленным содержимым `children`.

```jsx
const Mailto = ({ email, subject = "", body = "", children }) => {
  const params =
    subject || body
      ? `?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(
          body
        )}`
      : "";

  return <a href={`mailto:${email}${params}`}>{children}</a>;
};
```

Пример использования:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Mailto email="foo@bar.baz" subject="Hello & Welcome" body="Hello world!">
    Mail me!
  </Mailto>
);
```

Нажмите на кнопку 'Go Live' в правом нижнем углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы предварительно просмотреть веб-страницу.
