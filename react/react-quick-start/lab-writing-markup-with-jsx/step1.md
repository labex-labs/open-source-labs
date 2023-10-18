# Writing Markup With JSX

> The React project have already been provided in the VM. In general, you only need to add code to `App.js`.

Please use the following command to install the dependencies:

```bash
npm i
```

The markup syntax you’ve seen above is called JSX. It is optional, but most React projects use JSX for its convenience.

JSX is stricter than HTML. You have to close tags like `<br />`. Your component also can’t return multiple JSX tags. You have to wrap them into a shared parent, like a `<h1>...</h1>` or an empty `<>...</>` wrapper:

```js
// App.js
export default function Profile() {
  return (
    <>
      <h1>Hedy Lamarr</h1>
    </>
  );
}
```

If you have a lot of HTML to port to JSX, you can use an [online converter](https://transform.tools/html-to-jsx).

To run the project, use the following command. Then, you can refresh the **Web 8080** Tab to preview the web page.

```bash
npm start
```
