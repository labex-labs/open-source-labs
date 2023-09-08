# How jQuery Works

> `index.html` have already been provided in the VM.

This file will be automatically generated during the environment initialization. If it is not automatically generated, create the file and function as shown in the image above. The function code is as follows:

```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Demo</title>
  </head>
  <body>
    <p>jQuery</p>
    <script src="jquery.min.js"></script>
    <script>
      // Your code goes here.
    </script>
  </body>
</html>
```

The `src` attribute in the `<script>` element must point to a copy of jQuery. Download a copy of jQuery from the [Downloading jQuery](https://jquery.com/download/) page and store the `jquery.min.js` file in the same directory as your HTML file.

> Note: When you download jQuery, the file name may contain a version number, e.g., `jquery-x.y.z.js`. Make sure to either rename this file to `jquery.js` or update the `src` attribute of the `<script>` element to match the file name.

#### Launching Code on Document Ready

To ensure that their code runs after the browser finishes loading the document, many JavaScript programmers wrap their code in an `onload` function:

```js
window.onload = function () {
  alert("welcome");
};
```

Unfortunately, the code doesn't run until all images are finished downloading, including banner ads. To run code as soon as the document is ready to be manipulated, jQuery has a statement known as the [ready event](http://api.jquery.com/ready/):

```js
$(document).ready(function () {
  // Your code here.
});
```

> Note: The jQuery library exposes its methods and properties via two properties of the `window` object called `jQuery` and `$`. `$` is simply an alias for `jQuery` and it's often employed because it's shorter and faster to write.

For example, inside the ready event, you can add a click handler to the link:

```js
$(document).ready(function () {
  $("button").click(function () {
    $("p").text("Hello jQuery!");
  });
});
```

Copy the above jQuery code into your HTML file where it says `// Your code goes here`. Then, save your HTML file and reload the test page in your browser.

#### Complete Example

The following example illustrates the click handling code discussed above, embedded directly in the HTML `<body>`. Note that in practice, it is usually better to place your code in a separate JS file and load it on the page with a `<script>` element's `src` attribute.

```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Demo</title>
  </head>
  <body>
    <button>click me</button>
    <p>Hello World</p>
    <script src="jquery.min.js"></script>
    <script>
      $(document).ready(function () {
        $("button").click(function () {
          $("p").text("Hello jQuery!");
        });
      });
    </script>
  </body>
</html>
```

> Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
