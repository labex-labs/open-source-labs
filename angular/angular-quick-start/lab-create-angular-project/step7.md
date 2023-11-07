# Add Styling (Optional)

Every Angular component can have its own styles. The styles specified in `hello-world.component.css` will only affect `HelloWorldComponent` and won't "leak" to other parts of the application. This encapsulation is a part of the Angular View Encapsulation feature, which emulates the behavior of Shadow DOM by default.

If you want to add some styles to your `hello-world` component, you can edit the `hello-world.component.css` file:

```css
/* This is the hello-world.component.css file */
p {
  color: green;
  font-size: 20px;
}
```
