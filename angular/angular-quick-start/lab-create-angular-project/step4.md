# Create a New Component

Components are the main building block for Angular applications. Each component consists of:

- An HTML template that declares what renders on the page
- A TypeScript class that defines behavior
- A CSS selector that defines how the component is used in a template
- Optionally, CSS styles applied to the template

Let's create a new component named `hello-world`.

```sh
ng generate component hello-world
```

The `generate` (or just `g`) command creates a new directory with all the files you need:

```txt
my-angular-app/
  src/
    app/
      hello-world/
        hello-world.component.css
        hello-world.component.html
        hello-world.component.spec.ts
        hello-world.component.ts
```

- `hello-world.component.css`: The component's private CSS styles.
- `hello-world.component.html`: The component template, written in HTML.
- `hello-world.component.spec.ts`: The component's test specifications.
- `hello-world.component.ts`: The component class code, written in TypeScript.
