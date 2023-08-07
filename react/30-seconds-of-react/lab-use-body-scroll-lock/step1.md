# React useBodyScrollLock Hook

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

This code snippet allows users to lock the body scroll when a modal is open. Here's how it works:

First, the `useBodyScrollLock` function is defined, which uses the `useLayoutEffect` hook to lock the scroll of the `body` element. This hook runs only once when the component is mounted, and it sets the `overflow` value of the `body` element to `'hidden'`. When the component is unmounted, the original `overflow` value is restored.

```jsx
const useBodyScrollLock = () => {
  React.useLayoutEffect(() => {
    const originalStyle = window.getComputedStyle(document.body).overflow;
    document.body.style.overflow = "hidden";
    return () => (document.body.style.overflow = originalStyle);
  }, []);
};
```

Then, the `Modal` component is defined, which utilizes the `useBodyScrollLock` function. This component displays a message in a box that is centered on the screen. When the box is clicked, the modal is closed and the body scroll is unlocked.

```jsx
const Modal = ({ onClose }) => {
  useBodyScrollLock();

  return (
    <div
      style={{
        zIndex: 100,
        background: "rgba(0,0,0,0.25)",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
      }}
      onClick={onClose}
    >
      <p style={{ padding: 8, borderRadius: 8, background: "#fff" }}>
        Scroll locked! <br /> Click me to unlock
      </p>
    </div>
  );
};
```

Finally, the `MyApp` component is defined, which renders a button that opens the `Modal` component when clicked.

```jsx
const MyApp = () => {
  const [modalOpen, setModalOpen] = React.useState(false);

  return (
    <div
      style={{
        height: "400vh",
        textAlign: "center",
        paddingTop: 100,
        background: "linear-gradient(to bottom, #1fa2ff, #12d8fa, #a6ffcb)",
      }}
    >
      <button onClick={() => setModalOpen(true)}>Open modal</button>
      {modalOpen && <Modal onClose={() => setModalOpen(false)} />}
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
