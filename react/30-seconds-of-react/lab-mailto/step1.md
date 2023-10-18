# Email Link

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

This function creates a link that, when clicked, opens the user's email client and populates a new email with specified subject and body content. The link is formatted using the `mailto:` protocol.

To use the function, provide an `email` prop with the recipient's email address, and optionally provide `subject` and `body` props to populate the email with initial content. These props are safely encoded using `encodeURIComponent` before being added to the link URL.

The link is rendered with the provided `children` as its content.

```jsx
const Mailto = ({ email, subject = "", body = "", children }) => {
  const params =
    subject || body
      ? `?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(
          body
        )}`
      : "";

  return <a href={`mailto:${email}${params}`}>{children}</a>;
};
```

Example usage:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Mailto email="foo@bar.baz" subject="Hello & Welcome" body="Hello world!">
    Mail me!
  </Mailto>
);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
