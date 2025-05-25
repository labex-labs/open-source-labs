# 문자열을 URL 슬러그로 변환하는 함수

URL 에서 사용할 수 있는 슬러그로 문자열을 변환하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `String.prototype.toLowerCase()` 및 `String.prototype.trim()` 메서드를 사용하여 문자열을 정규화합니다.
3. `String.prototype.replace()` 메서드를 사용하여 공백, 대시, 밑줄을 `-`로 바꾸고 특수 문자를 제거합니다.
4. 다음 코드를 구현합니다.

```js
const slugify = (str) =>
  str
    .toLowerCase()
    .trim()
    .replace(/[^\w\s-]/g, "")
    .replace(/[\s_-]+/g, "-")
    .replace(/^-+|-+$/g, "");
```

5. `slugify('Hello World!');` 입력을 사용하여 함수를 테스트하면 `'hello-world'` 출력이 반환되어야 합니다.
