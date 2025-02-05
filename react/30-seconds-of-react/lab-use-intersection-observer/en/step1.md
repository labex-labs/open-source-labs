# React useIntersectionObserver Hook

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

To observe visibility changes for a given element, follow these steps:

1. Use the `useState()` hook to store the intersection value of the given element.
2. Create an `IntersectionObserver` with the given `options` and an appropriate callback to update the `isIntersecting` state variable.
3. Use the `useEffect()` hook to call `IntersectionObserver.observe()` when mounting the component and clean up using `IntersectionObserver.unobserve()` when unmounting.

Here's an example implementation:

```jsx
const useIntersectionObserver = (ref, options) => {
  const [isIntersecting, setIsIntersecting] = React.useState(false);

  React.useEffect(() => {
    const observer = new IntersectionObserver(([entry]) => {
      setIsIntersecting(entry.isIntersecting);
    }, options);

    if (ref.current) {
      observer.observe(ref.current);
    }

    return () => {
      observer.unobserve(ref.current);
    };
  }, [ref, options]);

  return isIntersecting;
};
```

You can use the `useIntersectionObserver` hook like this:

```jsx
const MyApp = () => {
  const ref = React.useRef();
  const onScreen = useIntersectionObserver(ref, { threshold: 0.5 });

  return (
    <div>
      <div style={{ height: "100vh" }}>Scroll down</div>
      <div style={{ height: "100vh" }} ref={ref}>
        <p>{onScreen ? "Element is on screen." : "Scroll more!"}</p>
      </div>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
