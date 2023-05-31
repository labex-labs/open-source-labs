# How to Smoothly Scroll an Element into View with JavaScript

To smoothly scroll an element into view in a web page, you can use JavaScript's `Element.scrollIntoView()` method. This method scrolls the element on which it's called into the visible area of the browser window. To make the scroll smooth, you can pass the option `{ behavior: 'smooth' }`.

Here's an example code snippet that defines a function called `smoothScroll` that takes an element selector and scrolls it smoothly into view:

```js
const smoothScroll = (element) => {
  document.querySelector(element).scrollIntoView({
    behavior: "smooth",
  });
};
```

To use this function, you can call it with an element selector as an argument. For example:

```js
smoothScroll("#fooBar"); // scrolls smoothly to the element with the id fooBar
smoothScroll(".fooBar"); // scrolls smoothly to the first element with a class of fooBar
```

To start practicing coding with JavaScript, you can open the Terminal or SSH on your computer and type `node`.
