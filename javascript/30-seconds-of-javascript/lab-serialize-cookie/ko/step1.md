# 쿠키 직렬화 방법

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오. 그런 다음 다음 단계를 따라 쿠키 이름 - 값 쌍을 Set-Cookie 헤더 문자열로 직렬화하십시오.

1. 템플릿 리터럴과 `encodeURIComponent()`를 사용하여 적절한 문자열을 생성합니다.
2. `name` 및 `val` 매개변수를 전달하여 `serializeCookie` 함수를 구현합니다.
3. 이 함수는 적절하게 직렬화된 문자열을 반환합니다.

다음은 `serializeCookie` 함수를 사용하는 예입니다.

```js
const serializeCookie = (name, val) =>
  `${encodeURIComponent(name)}=${encodeURIComponent(val)}`;

serializeCookie("foo", "bar"); // 'foo=bar'
```

이 예에서 `serializeCookie` 함수는 쿠키 이름으로 `foo`를, 쿠키 값으로 `bar`를 입력받아 `foo=bar`의 직렬화된 쿠키 문자열을 반환합니다.
