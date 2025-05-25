# 쿼리 문자열을 객체로 변환하기

쿼리 문자열 또는 URL 을 객체로 변환하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `String.prototype.split()`을 사용하여 주어진 `url`에서 매개변수를 추출합니다.
3. `URLSearchParams` 생성자를 사용하여 객체를 생성하고 스프레드 연산자 (`...`) 를 사용하여 키 - 값 쌍의 배열로 변환합니다.
4. `Array.prototype.reduce()`를 사용하여 키 - 값 쌍의 배열을 객체로 변환합니다.

쿼리 문자열을 변환하는 코드는 다음과 같습니다.

```js
const queryStringToObject = (url) =>
  [...new URLSearchParams(url.split("?")[1])].reduce(
    (a, [k, v]) => ((a[k] = v), a),
    {}
  );
```

사용 예시:

```js
queryStringToObject("https://google.com?page=1&count=10");
// {page: '1', count: '10'}
```
