# Automatic Text Linking

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

This component renders a string as plaintext, with URLs converted to appropriate link elements.

To achieve this, it uses `String.prototype.split()` and `String.prototype.match()` with a regular expression to find URLs in the given string. The matched URLs are then returned as `<a>` elements, dealing with missing protocol prefixes if necessary. The remaining parts of the string are rendered as plaintext.

Here is the code:

```jsx
const AutoLink = ({ text }) => {
  const urlRegex =
    /((?:https?:\/\/)?(?:(?:[a-z0-9]?(?:[a-z0-9\-]{1,61}[a-z0-9])?\.[^\.|\s])+[a-z\.]*[a-z]+|(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3})(?::\d{1,5})*[a-z0-9.,_\/~#&=;%+?\-\\(\\)]*)/gi;

  const renderText = () => {
    return text.split(urlRegex).map((word, index) => {
      const urlMatch = word.match(urlRegex);
      if (urlMatch) {
        const url = urlMatch[0];
        return (
          <a key={index} href={url.startsWith("http") ? url : `http://${url}`}>
            {url}
          </a>
        );
      }
      return <span key={index}>{word}</span>;
    });
  };

  return <div>{renderText()}</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <AutoLink text="foo bar baz http://example.org bar" />,
);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
