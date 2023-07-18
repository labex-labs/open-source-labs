# HTTP Get Request

To make a GET request to a given URL in JavaScript using `XMLHttpRequest` web API, follow the steps below:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `httpGet` function provided below to make the GET request.
3. Pass the URL as the first argument to the `httpGet` function.
4. Pass the `callback` function as the second argument to handle the `onload` event and receive the `responseText`.
5. Pass the `err` function as the third argument to handle the `onerror` event. If you omit the third argument, errors will be logged to the console's `error` stream by default.

```js
const httpGet = (url, callback, err = console.error) => {
  const request = new XMLHttpRequest();
  request.open("GET", url, true);
  request.onload = () => callback(request.responseText);
  request.onerror = () => err(request);
  request.send();
};
```

To test the `httpGet` function, use the following code:

```js
httpGet("https://jsonplaceholder.typicode.com/posts/1", console.log); /*
Logs: {
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}
*/
```
