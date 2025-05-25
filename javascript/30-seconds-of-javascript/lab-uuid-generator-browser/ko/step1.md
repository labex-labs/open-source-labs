# 브라우저에서 UUID 생성하기

[RFC4122](https://www.ietf.org/rfc/rfc4122.txt) 버전 4 에 호환되는 UUID 를 브라우저에서 생성하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력합니다.
2. `Crypto.getRandomValues()` 메서드를 사용하여 UUID 를 생성합니다.
3. `Number.prototype.toString()` 메서드를 사용하여 UUID 를 16 진수 문자열로 변환합니다.
4. 다음 코드를 구현합니다.

```js
const UUIDGeneratorBrowser = () =>
  ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, (c) =>
    (
      c ^
      (crypto.getRandomValues(new Uint8Array(1))[0] & (15 >> (c / 4)))
    ).toString(16)
  );
```

5. `UUIDGeneratorBrowser()` 함수를 호출하여 UUID 를 생성합니다. 예를 들어, `UUIDGeneratorBrowser()`는 `'7982fcfe-5721-4632-bede-6000885be57d'`를 반환합니다.
