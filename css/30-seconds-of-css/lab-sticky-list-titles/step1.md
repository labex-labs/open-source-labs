# Code for Creating a List with Sticky Headings

To create a list with sticky headings, follow these steps:

1. In your HTML file, add a container div with a class of "container" and a list with a class of "sticky-stack".
2. Set the overflow-y property of the list to auto.
3. Set the position of each heading (dt) to sticky and set the top property to 0.
4. Add the necessary styling to your CSS file.

Here is an example code block:

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
