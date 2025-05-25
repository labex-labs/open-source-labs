# 객체를 쿼리 문자열로 변환하기

객체를 쿼리 문자열로 변환하려면, 주어진 객체의 key-value 쌍으로부터 쿼리 문자열을 생성하는 `objectToQueryString()` 함수를 사용합니다.

이 함수는 다음과 같이 작동합니다:

- `queryParameters`로부터 쿼리 문자열을 생성하기 위해 `Object.entries()`에 `Array.prototype.reduce()`를 사용합니다.
- `queryString`의 길이에 따라 `symbol`을 `?` 또는 `&`로 결정합니다.
- `val`이 문자열인 경우에만 `queryString`에 연결합니다.
- `queryParameters`가 falsy 한 경우 `queryString` 또는 빈 문자열을 반환합니다.

`objectToQueryString()` 함수의 코드는 다음과 같습니다:

```js
const objectToQueryString = (queryParameters) => {
  return queryParameters
    ? Object.entries(queryParameters).reduce(
        (queryString, [key, val], index) => {
          const symbol = queryString.length === 0 ? "?" : "&";
          queryString +=
            typeof val === "string" ? `${symbol}${key}=${val}` : "";
          return queryString;
        },
        ""
      )
    : "";
};
```

`objectToQueryString()` 함수의 사용 예시:

```js
objectToQueryString({ page: "1", size: "2kg", key: undefined }); // returns '?page=1&size=2kg'
```
