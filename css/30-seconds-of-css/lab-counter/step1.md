# Counter

`index.html` and `style.css` have already been provided in the VM.

To create a custom list counter that accounts for nested list elements, follow these steps:

1. Use `counter-reset` to initialize a variable counter (default `0`), with the name being the value of the attribute (e.g. `counter`).
2. Use `counter-increment` on the variable counter for each countable element (e.g. each `<li>`).
3. Use `counters()` to display the value of each variable counter as part of the `content` of the `::before` pseudo-element for each countable element (e.g. each `<li>`). The second value passed to it (`'.'`) acts as the delimiter for nested counters.

Here is an example HTML code:

```html
<ul>
  <li>List item</li>
  <li>List item</li>
  <li>
    List item
    <ul>
      <li>List item</li>
      <li>List item</li>
      <li>List item</li>
    </ul>
  </li>
</ul>
```

And here is the CSS code to apply the custom list counter:

```css
ul {
  counter-reset: counter;
  list-style: none;
}

li::before {
  counter-increment: counter;
  content: counters(counter, ".") " ";
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
