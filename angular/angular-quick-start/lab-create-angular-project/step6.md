# Use the New Component

The selector of the `HelloWorldComponent` is `app-hello-world`. You use this selector to include the component in other components' templates. Here we add `<app-hello-world></app-hello-world>` to `app.component.html`, which is the main application view. Angular then inserts an instance of `HelloWorldComponent` into the `AppComponent`'s view, exactly where you placed the tag.

Open `app.component.html` and add your `hello-world` component to the template using its selector:

```html
<!-- This is the app.component.html file -->
<app-hello-world></app-hello-world>
```
