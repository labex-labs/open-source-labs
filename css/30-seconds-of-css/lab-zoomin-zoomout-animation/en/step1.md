# Understanding HTML Structure

Before we start creating our animation, we need to understand the HTML structure we will be working with. In this step, we will examine the provided HTML file and make any necessary modifications.

1. Open the `index.html` file in the editor.

2. If the file is empty or missing, create it with the following content:

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Zoom In Zoom Out Animation</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <h1>CSS Animation Demo</h1>
    <p>This box demonstrates a zoom in zoom out animation:</p>

    <div class="zoom-in-out-box"></div>
  </body>
</html>
```

3. Let's understand what this HTML does:
   - We have a standard HTML document structure with a title and viewport settings
   - We link to an external CSS file named `style.css`
   - We include a heading and paragraph to explain our demo
   - Most importantly, we have a `<div>` element with class `zoom-in-out-box` that will be animated

4. Save the `index.html` file if you made any changes.

This div element will be our canvas for creating the animation. In the next step, we will style this element using CSS.
