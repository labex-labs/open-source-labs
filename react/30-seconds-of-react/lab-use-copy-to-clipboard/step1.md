# React useCopyToClipboard Hook

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

To copy the given text to the clipboard, use the `copyToClipboard` snippet provided in `/js/s/copy-to-clipboard/` along with the `useState()` hook to initialize the `copied` variable. To create a callback for the `copyToClipboard` method, use the `useCallback()` hook. To reset the `copied` state variable when the `text` changes, use the `useEffect()` hook. Finally, return the `copied` state variable and the `copy` callback.

The following code demonstrates an example of how to use these hooks and methods to create a `TextCopy` component. When the user clicks the "Click to copy" button, the `copy` function is called and the `copied` variable is set to `true`. If the copy is successful, "Copied!" will be displayed.

```jsx
const useCopyToClipboard = (text) => {
  const copyToClipboard = (str) => {
    const el = document.createElement("textarea");
    el.value = str;
    el.setAttribute("readonly", "");
    el.style.position = "absolute";
    el.style.left = "-9999px";
    document.body.appendChild(el);
    const selected =
      document.getSelection().rangeCount > 0
        ? document.getSelection().getRangeAt(0)
        : false;
    el.select();
    const success = document.execCommand("copy");
    document.body.removeChild(el);
    if (selected) {
      document.getSelection().removeAllRanges();
      document.getSelection().addRange(selected);
    }
    return success;
  };

  const [copied, setCopied] = React.useState(false);

  const copy = React.useCallback(() => {
    if (!copied) setCopied(copyToClipboard(text));
  }, [text]);

  React.useEffect(() => () => setCopied(false), [text]);

  return [copied, copy];
};

const TextCopy = (props) => {
  const [copied, copy] = useCopyToClipboard("Lorem ipsum");

  return (
    <div>
      <button onClick={copy}>Click to copy</button>
      <span>{copied && "Copied!"}</span>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<TextCopy />);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
