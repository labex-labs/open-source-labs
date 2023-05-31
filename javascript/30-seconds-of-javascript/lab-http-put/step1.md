# HTTP Put Request

To make a `PUT` request to a specified URL using `XMLHttpRequest` web API, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Create a function `httpPut` that takes four arguments: `url`, `data`, `callback`, and `err`.
3. Inside the `httpPut` function, create a new `XMLHttpRequest` object.
4. Use the `open` method to set up the `PUT` request with the passed `url`.
5. Use the `setRequestHeader` method to set the value of an `HTTP` request header.
6. Handle the `onload` event by running the provided `callback` function.
7. Handle the `onerror` event by running the provided `err` function, or omit the last argument, `err`, to log the request to the console's error stream by default.
8. Use the `send` method to send the `data` to the specified `url`.
9. In your code, create a `data` variable that contains a JSON string with the data to be sent in the request.
10. Call the `httpPut` function with the `url`, `data`, and a callback function that logs the response to the console.

Here's the updated code:

```js
const httpPut = (url, data, callback, err = console.error) => {
  const request = new XMLHttpRequest();
  request.open("PUT", url, true);
  request.setRequestHeader("Content-type", "application/json; charset=utf-8");
  request.onload = () => callback(request);
  request.onerror = () => err(request);
  request.send(data);
};

const password = "fooBaz";
const data = JSON.stringify({
  id: 1,
  title: "foo",
  body: "bar",
  userId: 1,
});

httpPut("https://jsonplaceholder.typicode.com/posts/1", data, (request) => {
  console.log(request.responseText);
}); /*
Logs: {
  id: 1,
  title: 'foo',
  body: 'bar',
  userId: 1
}
*/
```
