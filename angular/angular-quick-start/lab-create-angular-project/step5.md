# Modify the Component

In the component TypeScript class (`hello-world.component.ts`), we declare a property named message and assign it a string.

In Angular, component data can be displayed in the component's template by using the double curly braces `{{ }}`, which is Angular's interpolation binding syntax. This syntax tells Angular to replace the contents inside the curly braces with the value of the property.

1. Open `hello-world.component.ts` and add a property:

```typescript
import { Component, OnInit } from "@angular/core";

@Component({
  selector: "app-hello-world",
  templateUrl: "./hello-world.component.html",
  styleUrls: ["./hello-world.component.css"],
})
export class HelloWorldComponent implements OnInit {
  message: string = "Hello, Angular World!";

  constructor() {}

  ngOnInit(): void {}
}
```

2. Edit `hello-world.component.html` to display the `message` property:

```html
<p>{{ message }}</p>
```
