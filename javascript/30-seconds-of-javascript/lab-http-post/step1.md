# HTTP Post Request with XMLHttpRequest

To make a `POST` request to a URL using `XMLHttpRequest`, use the following steps:

1. Call the `httpPost` function with the URL, data, and callback function as arguments.
2. The `httpPost` function creates a new `XMLHttpRequest` object and sets up the request with the `open` method.
3. Use the `setRequestHeader` method to set the value of the `Content-type` header to `application/json; charset=utf-8`.
4. Handle the `onload` event by calling the provided `callback` function with the `responseText` as an argument.
5. Handle the `onerror` event by running the provided `err` function.
6. If the `err` argument is omitted, errors will be logged to the console's `error` stream by default.
7. Call the `send` method on the `XMLHttpRequest` object with the `data` argument.

```js
const httpPost = (url, data, callback, err = console.error) => {
  const request = new XMLHttpRequest();
  request.open("POST", url, true);
  request.setRequestHeader("Content-type", "application/json; charset=utf-8");
  request.onload = () => callback(request.responseText);
  request.onerror = () => err(request);
  request.send(data);
};
```

Here is an example of how to use the `httpPost` function:

```js
const newPost = {
  userId: 1,
  id: 1337,
  title: "Foo",
  body: "bar bar bar",
};
const data = JSON.stringify(newPost);
httpPost("https://jsonplaceholder.typicode.com/posts", data, console.log); /*
Logs: {
  "userId": 1,
  "id": 1337,
  "title": "Foo",
  "body": "bar bar bar"
}
*/

httpPost(
  "https://jsonplaceholder.typicode.com/posts",
  null, // does not send a body
  console.log
); /*
Logs: {
  "id": 101
}
*/
```
