# Textarea With Character Limit

> `index.html` and `script.js` have already been provided in the VM.. In general, you only need to add code to `script.js` and `style.css`.

Here's a revised version of the code that is clearer, more concise, and more coherent:

```jsx
const LimitedTextarea = ({ rows, cols, value, limit }) => {
  const [content, setContent] = React.useState(value.slice(0, limit));

  const setFormattedContent = React.useCallback(
    (text) => {
      setContent(text.slice(0, limit));
    },
    [limit]
  );

  return (
    <>
      <textarea
        rows={rows}
        cols={cols}
        onChange={(event) => setFormattedContent(event.target.value)}
        value={content}
      />
      <p>
        {content.length}/{limit}
      </p>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <LimitedTextarea limit={32} value="Hello!" />
);
```

In this revised code, we:

- Simplified the comments to provide a more concise overview of what each part of the code does.
- Removed unnecessary code comments.
- Removed the `setContent` function from the `useCallback` dependency array, as it doesn't need to be there.
- Added parentheses around the `text` argument in the `useCallback` function for consistency.
- Used arrow functions for the `onChange` event handler for brevity.

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
