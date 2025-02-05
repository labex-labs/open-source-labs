# List With Sticky Section Headings

`index.html` and `style.css` have already been provided in the VM.

To create a list with sticky headings for each section, follow these steps:

1. Allow the list container (`<dl>`) to overflow vertically by using `overflow-y: auto`.
2. Stick the headings (`<dt>`) to the top of the container by setting their `position` to `sticky` and applying `top: 0`.
3. Use the following HTML and CSS code:

HTML:

```html
<div class="container">
  <dl class="sticky-stack">
    <dt>A</dt>
    <dd>Algeria</dd>
    <dd>Angola</dd>

    <dt>B</dt>
    <dd>Benin</dd>
    <dd>Botswana</dd>
    <dd>Burkina Faso</dd>
    <dd>Burundi</dd>

    <dt>C</dt>
    <dd>Cabo Verde</dd>
    <dd>Cameroon</dd>
    <dd>Central African Republic</dd>
    <dd>Chad</dd>
    <dd>Comoros</dd>
    <dd>Congo, Democratic Republic of the</dd>
    <dd>Congo, Republic of the</dd>
    <dd>Cote d'Ivoire</dd>

    <dt>D</dt>
    <dd>Djibouti</dd>

    <dt>E</dt>
    <dd>Egypt</dd>
    <dd>Equatorial Guinea</dd>
    <dd>Eritrea</dd>
    <dd>Eswatini (formerly Swaziland)</dd>
    <dd>Ethiopia</dd>
  </dl>
</div>
```

CSS:

```css
.container {
  display: grid;
  place-items: center;
  min-height: 400px;
}

.sticky-stack {
  background: #37474f;
  color: #fff;
  margin: 0;
  height: 320px;
  border-radius: 1rem;
  overflow-y: auto;
}

.sticky-stack dt {
  position: sticky;
  top: 0;
  font-weight: bold;
  background: #263238;
  color: #cfd8dc;
  padding: 0.25rem 1rem;
}

.sticky-stack dd {
  margin: 0;
  padding: 0.75rem 1rem;
}

.sticky-stack dd + dt {
  margin-top: 1rem;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
