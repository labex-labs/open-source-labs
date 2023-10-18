# Callable Telephone Link

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

To create a link that calls a phone number, use the `Callto` component. This component creates an `<a>` element with an appropriate `href` attribute. To render the link, specify the phone number using the `phone` prop, and the link text using the `children` prop.

```jsx
const Callto = ({ phone, children }) => {
  return <a href={`tel:${phone}`}>{children}</a>;
};
```

To use the `Callto` component, call the `ReactDOM.render()` method and pass in the `Callto` element with the `phone` and `children` props set.

```jsx
ReactDOM.render(
  <Callto phone="+302101234567">Call me!</Callto>,
  document.getElementById("root")
);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
