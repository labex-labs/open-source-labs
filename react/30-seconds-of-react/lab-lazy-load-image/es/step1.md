# Imagen con carga diferida

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Para renderizar una imagen que admita la carga diferida, siga estos pasos:

1. Utilice el hook `useState()` para crear un valor con estado que indique si la imagen ha sido cargada.
2. Utilice el hook `useEffect()` para comprobar si `HTMLImageElement.prototype` contiene `'loading'`. Esto comprueba si la carga diferida está soportada nativamente. Si no es así, cree un nuevo `IntersectionObserver` y utilice `IntersectionObserver.observer()` para observar el elemento `<img>`. Utilice el valor devuelto por el hook para limpiar cuando el componente se desmonte.
3. Utilice el hook `useCallback()` para memoizar una función de devolución de llamada para el `IntersectionObserver`. Esta devolución de llamada actualizará la variable de estado `isLoaded` y utilizará `IntersectionObserver.disconnect()` para desconectar la instancia de `IntersectionObserver`.
4. Utilice el hook `useRef()` para crear dos referencias. Una contendrá el elemento `<img>` y la otra la instancia de `IntersectionObserver`, si es necesario.
5. Finalmente, renderice el elemento `<img>` con los atributos dados. Aplique `loading='lazy'` para que se cargue de manera diferida, si es necesario. Utilice `isLoaded` para determinar el valor del atributo `src`.

A continuación, se muestra una implementación de ejemplo de estos pasos:

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

Para utilizar este componente `LazyLoadImage`, simplemente llámelo con los atributos `src` y `alt` de la imagen:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <LazyLoadImage src="https://picsum.photos/id/1080/600/600" alt="Fresas" />
);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
