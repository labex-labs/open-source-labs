# React useClickOutside Hook

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

This code handles the event of clicking outside of a wrapped component. It works by creating a custom hook that takes a `ref` and a `callback` to handle the `click` event. The `useEffect()` hook is used to append and clean up the `click` event, while the `useRef()` hook is used to create a `ref` for the click component and pass it to the `useClickOutside` hook.

```jsx
const useClickOutside = (ref, callback) => {
  const handleClick = (e) => {
    if (ref.current && !ref.current.contains(e.target)) {
      callback();
    }
  };
  React.useEffect(() => {
    document.addEventListener("click", handleClick);
    return () => {
      document.removeEventListener("click", handleClick);
    };
  });
};

const ClickBox = ({ onClickOutside }) => {
  const clickRef = React.useRef();
  useClickOutside(clickRef, onClickOutside);
  return (
    <div
      className="click-box"
      ref={clickRef}
      style={{
        border: "2px dashed orangered",
        height: 200,
        width: 400,
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <p>Click out of this element</p>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <ClickBox onClickOutside={() => alert("click outside")} />
);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
