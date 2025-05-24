# Base64 인코딩된 문자열 디코딩

base-64 인코딩을 사용하여 인코딩된 데이터 문자열을 디코딩하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 주어진 문자열에 대해 base-64 인코딩을 사용하여 `Buffer`를 생성합니다.
3. `Buffer.prototype.toString()`을 사용하여 디코딩된 문자열을 반환합니다.

다음은 코드 스니펫 예시입니다.

```js
const atob = (str) => Buffer.from(str, "base64").toString("binary");
```

`atob('Zm9vYmFy')`를 실행하여 이 함수를 테스트할 수 있으며, 결과는 `'foobar'`여야 합니다.
