# 폼을 객체로 변환하기

코딩 연습을 위해 터미널/SSH 를 열고 `node`를 입력하세요. 다음 단계를 사용하여 일련의 폼 요소들을 객체로 인코딩할 수 있습니다.

1. `FormData` 생성자를 사용하여 HTML `form`을 `FormData`로 변환합니다.
2. `Array.from()`을 사용하여 `FormData`를 배열로 변환합니다.
3. `Array.prototype.reduce()`를 사용하여 배열에서 객체를 수집합니다.

다음은 코드 예시입니다.

```js
const formToObject = (form) =>
  Array.from(new FormData(form)).reduce(
    (acc, [key, value]) => ({
      ...acc,
      [key]: value
    }),
    {}
  );
```

특정 폼을 변환하려면 `formToObject` 함수를 호출하고 폼 요소를 인수로 전달하면 됩니다.

```js
formToObject(document.querySelector("#form"));
// { email: 'test@email.com', name: 'Test Name' }
```
