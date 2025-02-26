# React хук useIsomporphicEffect

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Для обеспечения правильного использования `useEffect()` на сервере и `useLayoutEffect()` на клиенте можно использовать `typeof`, чтобы проверить, определен ли объект `Window`. Если он определен, возвращаем `useLayoutEffect()`, в противном случае возвращаем `useEffect()`. Вот пример, как это можно реализовать:

```jsx
const useIsomorphicEffect =
  typeof window !== "undefined" ? React.useLayoutEffect : React.useEffect;
```

Затем в своем коде можно использовать `useIsomorphicEffect()`, как показано в этом примере:

```jsx
const MyApp = () => {
  useIsomorphicEffect(() => {
    window.console.log("Hello");
  }, []);

  return null;
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Это выведет 'Hello' в консоль при монтировании компонента и будет работать корректно как на сервере, так и на клиенте.

Пожалуйста, нажмите на кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем можно обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
