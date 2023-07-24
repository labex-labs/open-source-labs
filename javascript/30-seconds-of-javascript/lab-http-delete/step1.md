# HTTP DELETE Request

To make an HTTP DELETE request to a given URL using the `XMLHttpRequest` web API, use the `httpDelete` function. The function takes three arguments: `url` (the URL to make the request to), `callback` (a function to run when the request is successful), and `err` (a function to run when the request fails). If the `err` argument is omitted, the request will be logged to the console's error stream by default.

```js
const httpDelete = (url, callback, err = console.error) => {
  const request = new XMLHttpRequest();
  request.open("DELETE", url, true);
  request.onload = () => callback(request);
  request.onerror = () => err(request);
  request.send();
};
```

To use the `httpDelete` function, pass in the URL and the desired callback function as arguments. For example:

```js
httpDelete("https://jsonplaceholder.typicode.com/posts/1", (request) => {
  console.log(request.responseText);
}); // Logs: {}
```

To begin practicing coding, open the Terminal/SSH and type `node`.
