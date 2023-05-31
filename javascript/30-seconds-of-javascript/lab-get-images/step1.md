# Code Snippet: Getting All Images within an Element

To fetch all images from within an HTML element and store them in an array, you can use the code below:

```js
const getImages = (element, includeDuplicates = false) => {
  const images = [...element.getElementsByTagName("img")].map((img) =>
    img.getAttribute("src")
  );
  return includeDuplicates ? images : [...new Set(images)];
};
```

In this code:

- `element` is the HTML element in which you want to find the images.
- `includeDuplicates` is an optional argument that determines whether to include or exclude duplicate images from the result. If it is set to `true`, the function will return all images, including duplicates. If it is set to `false` or omitted, the function will return only the unique images.

To use this function, open the Terminal/SSH and type `node`. Then, call the function with the desired element and `includeDuplicates` value:

```js
getImages(document, true); // returns an array of all images within the document, including duplicates
getImages(document, false); // returns an array of all unique images within the document
```
