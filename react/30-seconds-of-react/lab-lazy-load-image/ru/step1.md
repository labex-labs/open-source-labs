# Отложенная загрузка изображений

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно добавить код только в `script.js` и `style.css`.

Чтобы отобразить изображение, поддерживающее отложенную загрузку, следуйте шагам:

1. Используйте хук `useState()`, чтобы создать состояние, которое будет показывать, загружено ли изображение.
2. Используйте хук `useEffect()`, чтобы проверить, содержит ли `HTMLImageElement.prototype` `'loading'`. Это проверяет, поддерживается ли отложенная загрузка встроенным способом. Если нет, создайте новый `IntersectionObserver` и используйте `IntersectionObserver.observer()` для наблюдения за элементом `<img>`. Используйте возвращаемое значение хука для очистки при размонтировании компонента.
3. Используйте хук `useCallback()`, чтобы мемоизировать функцию обратного вызова для `IntersectionObserver`. Этот обратный вызов обновит переменную состояния `isLoaded` и использует `IntersectionObserver.disconnect()` для отключения экземпляра `IntersectionObserver`.
4. Используйте хук `useRef()`, чтобы создать два ref. Один будет хранить элемент `<img>`, а другой — экземпляр `IntersectionObserver`, если это необходимо.
5. Наконец, отобразите элемент `<img>` с заданными атрибутами. Примените `loading='lazy'`, чтобы заставить его загружаться отложенно, если необходимо. Используйте `isLoaded`, чтобы определить значение атрибута `src`.

Вот пример реализации этих шагов:

```jsx
const LazyLoadImage = ({
  alt,
  src,
  className,
  loadInitially = false,
  observerOptions = { root: null, rootMargin: "200px 0px" },
  ...props
}) => {
  const observerRef = React.useRef(null);
  const imgRef = React.useRef(null);
  const [isLoaded, setIsLoaded] = React.useState(loadInitially);

  const observerCallback = React.useCallback(
    (entries) => {
      if (entries[0].isIntersecting) {
        observerRef.current.disconnect();
        setIsLoaded(true);
      }
    },
    [observerRef]
  );

  React.useEffect(() => {
    if (loadInitially) return;

    if ("loading" in HTMLImageElement.prototype) {
      setIsLoaded(true);
      return;
    }

    observerRef.current = new IntersectionObserver(
      observerCallback,
      observerOptions
    );
    observerRef.current.observe(imgRef.current);
    return () => {
      observerRef.current.disconnect();
    };
  }, []);

  return (
    <img
      alt={alt}
      src={isLoaded ? src : ""}
      ref={imgRef}
      className={className}
      loading={loadInitially ? undefined : "lazy"}
      {...props}
    />
  );
};
```

Чтобы использовать этот компонент `LazyLoadImage`, просто вызовите его с атрибутами `src` и `alt` изображения:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <LazyLoadImage
    src="https://picsum.photos/id/1080/600/600"
    alt="Strawberries"
  />
);
```

Пожалуйста, нажмите кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
