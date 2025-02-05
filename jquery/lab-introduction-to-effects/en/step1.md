# Showing and Hiding Content

> `index.html` have already been provided in the VM.

jQuery can show or hide content instantaneously with `.show()` or `.hide()`:

```js
// Instantaneously hide all paragraphs
$("p").hide();

// Instantaneously show all divs that have the hidden style class
$("div.hidden").show();
```

When jQuery hides an element, it sets its CSS `display` property to `none`. This means the content will have zero width and height; it does not mean that the content will simply become transparent and leave an empty area on the page.

jQuery can also show or hide content by means of animation effects. You can tell `.show()` and `.hide()` to use animation in a couple of ways. One is to pass in an argument of `'slow'`, `'normal'`, or `'fast'`:

```js
// Slowly hide all paragraphs
$("p").hide("slow");

// Quickly show all divs that have the hidden style class
$("div.hidden").show("fast");
```

If you prefer more direct control over the duration of the animation effect, you can pass the desired duration in milliseconds to `.show()` and `.hide()`:

```js
// Hide all paragraphs over half a second
$("p").hide(2000);

// Show all divs that have the hidden style class over 1.25 seconds
$("div.hidden").show(1250);
```

Most developers pass in a number of milliseconds to have more precise control over the duration.

> Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
