# Revised Output

To copy a string to the clipboard, use the following function:

```js
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
  document.execCommand("copy");
  document.body.removeChild(el);
  if (selected) {
    document.getSelection().removeAllRanges();
    document.getSelection().addRange(selected);
  }
};
```

To use it, simply call `copyToClipboard('Lorem ipsum')`, where `'Lorem ipsum'` is the string you want to copy. Note that the function will only work if called from within a user action, such as a `click` event listener.

Alternatively, you can use the asynchronous [Clipboard API](https://developer.mozilla.org/en-US/docs/Web/API/Clipboard_API) in most current browsers. Check out the [copyToClipboardAsync snippet](/js/s/copy-to-clipboard-async) for more information.
