# Checking if the Environment is Travis CI

To check if you're running on Travis CI, use the `isTravisCI()` function. This function checks if the `TRAVIS` and `CI` environment variables are present.

```js
const isTravisCI = () => "TRAVIS" in process.env && "CI" in process.env;
```

To start coding on Travis CI, open the Terminal/SSH and type `node`.
