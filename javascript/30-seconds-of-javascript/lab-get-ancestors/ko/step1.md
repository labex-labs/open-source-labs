# 요소 조상 검색

문서 루트에서 지정된 요소까지의 요소 조상을 검색하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Node.parentNode`와 `while` 루프를 사용하여 요소의 조상 트리를 위로 이동합니다.
3. `Array.prototype.unshift()`를 사용하여 각 새로운 조상을 배열의 시작 부분에 추가합니다.

위 단계를 구현하는 샘플 코드는 다음과 같습니다.

```js
const getAncestors = (el) => {
  let ancestors = [];
  while (el) {
    ancestors.unshift(el);
    el = el.parentNode;
  }
  return ancestors;
};
```

특정 요소의 조상을 검색하려면 `querySelector()` 메서드를 사용하여 요소를 선택하고 이를 `getAncestors()` 함수에 인수로 전달합니다. 예를 들어:

```js
getAncestors(document.querySelector("nav"));
// [document, html, body, header, nav]
```

이렇게 하면 문서 루트에서 요소 자체까지의 순서로 지정된 요소의 모든 조상 배열이 반환됩니다.
