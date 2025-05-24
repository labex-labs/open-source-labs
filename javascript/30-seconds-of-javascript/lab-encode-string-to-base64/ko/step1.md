# 문자열을 Base64 로 인코딩하기

String 객체를 base64 로 인코딩된 ASCII 문자열로 인코딩하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩을 시작합니다.
2. 주어진 문자열과 이진 인코딩을 사용하여 `Buffer`를 생성합니다.
3. `Buffer.prototype.toString()`을 사용하여 base64 로 인코딩된 문자열을 반환합니다.

다음은 코드 스니펫 예시입니다.

```js
const encodeToBase64 = (str) => Buffer.from(str, "binary").toString("base64");
```

이제 `encodeToBase64()` 함수를 사용하여 모든 문자열을 base64 로 인코딩할 수 있습니다. 예를 들어:

```js
encodeToBase64("foobar"); // 'Zm9vYmFy'
```
