# Adding Styles

In React, you specify a CSS class with `className`. It works the same way as the HTML [class](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/class) attribute:

```html
<img className="avatar" />
```

Then you write the CSS rules for it in a separate CSS file:

```css
/* App.css */
.avatar {
  border-radius: 50%;
}
```

React does not prescribe how you add CSS files. In the simplest case, you’ll add a `<link>` tag to your HTML. If you use a build tool or a framework, consult its documentation to learn how to add a CSS file to your project.

```js
// App.js
import "./App.css";
```

You can put more complex expressions inside the JSX curly braces too, for example, [string concatenation](https://javascript.info/operators#string-concatenation-with-binary):

```js
// App.js
const user = {
  name: "Hedy Lamarr",
  imageUrl: "https://i.imgur.com/yXOvdOSs.jpg",
  imageSize: 90,
};

export default function Profile() {
  return (
    <>
      <h1>{user.name}</h1>
      <img
        className="avatar"
        src={user.imageUrl}
        alt={"Photo of " + user.name}
        style={{
          width: user.imageSize,
          height: user.imageSize,
        }}
      />
    </>
  );
}
```

In the above example, `style={{}}` is not a special syntax, but a regular `{}` object inside the `style={ }` JSX curly braces. You can use the `style` attribute when your styles depend on JavaScript variables.
