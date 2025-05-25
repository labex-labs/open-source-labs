# 배열을 플래그 객체로 변환하기

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하세요.

다음 함수는 문자열 배열을 `true`로 매핑하는 객체로 변환합니다.

이를 위해 `Array.prototype.reduce()`를 사용합니다. 이 메서드는 배열을 객체로 변환하며, 여기서 각 배열 값은 값이 `true`로 설정된 키 역할을 합니다.

```js
const flags = (arr) => arr.reduce((acc, str) => ({ ...acc, [str]: true }), {});
```

다음은 예시입니다.

```js
flags(["red", "green"]); // { red: true, green: true }
```
