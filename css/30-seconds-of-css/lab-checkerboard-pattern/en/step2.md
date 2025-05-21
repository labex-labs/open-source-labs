# Creating the HTML Structure

Now that we understand our project files, let's create the HTML structure for our checkerboard pattern.

1. Open the `index.html` file in the editor again.

2. We need to add a container element for our checkerboard pattern. Inside the `<body>` tag, replace the comment with a `<div>` element that has a class of "checkerboard":

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Checkerboard Pattern</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <div class="checkerboard"></div>
  </body>
</html>
```

3. Save the `index.html` file by pressing Ctrl+S or clicking File > Save.

4. Now, let's add some basic CSS to define the dimensions of our checkerboard. Open the `style.css` file and add the following code:

```css
.checkerboard {
  width: 240px;
  height: 240px;
  background-color: #fff;
}
```

This CSS code does the following:

- Sets the width and height of our checkerboard to 240 pixels
- Sets the background color to white (#fff)

5. Save the `style.css` file.

6. Refresh the **Web 8080** tab to see the changes.

You should now see a white square with a width and height of 240 pixels. This will be the canvas for our checkerboard pattern.
