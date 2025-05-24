# 배열을 HTML 목록으로 변환하기

코딩을 시작하려면 터미널/SSH 를 실행하고 `node`를 입력하십시오.

이 함수는 주어진 배열 요소를 `<li>` 태그로 변환하고 주어진 ID 를 가진 목록에 추가합니다.

`Array.prototype.map()`과 `Document.querySelector()`를 사용하여 HTML 태그 목록을 생성합니다.

```js
const arrayToHTMLList = (arr, listID) =>
  (document.querySelector(`#${listID}`).innerHTML += arr
    .map((item) => `<li>${item}</li>`)
    .join(""));
```

사용 예시:

```js
arrayToHTMLList(["item 1", "item 2"], "myListID");
```
