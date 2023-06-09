# Lazy-Loading Image

> `index.html` and `script.js` have already been provided in the VM.. In general, you only need to add code to `script.js` and `style.css`.

To render an image that supports lazy loading, follow these steps:

1. Use the `useState()` hook to create a stateful value that indicates if the image has been loaded.
2. Use the `useEffect()` hook to check if the `HTMLImageElement.prototype` contains `'loading'`. This checks if lazy loading is supported natively. If not, create a new `IntersectionObserver` and use `IntersectionObserver.observer()` to observe the `<img>` element. Use the `return` value of the hook to clean up when the component unmounts.
3. Use the `useCallback()` hook to memoize a callback function for the `IntersectionObserver`. This callback will update the `isLoaded` state variable and use `IntersectionObserver.disconnect()` to disconnect the `IntersectionObserver` instance.
4. Use the `useRef()` hook to create two refs. One will hold the `<img>` element and the other the `IntersectionObserver` instance, if necessary.
5. Finally, render the `<img>` element with the given attributes. Apply `loading='lazy'` to make it load lazily, if necessary. Use `isLoaded` to determine the value of the `src` attribute.

Here's an example implementation of these steps:

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

To use this `LazyLoadImage` component, simply call it with the `src` and `alt` attributes of the image:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <LazyLoadImage
    src="https://picsum.photos/id/1080/600/600"
    alt="Strawberries"
  />
);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
