# JavaScript 에서 재귀를 사용하여 객체를 중첩하는 방법

평면 배열에서 객체를 재귀적으로 중첩하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 서로 연결된 객체를 중첩하기 위해 재귀를 사용합니다.
3. `id`가 `link`와 일치하는 항목을 필터링하기 위해 `Array.prototype.filter()`를 사용합니다.
4. 각 항목을 현재 항목의 자식인 항목을 기반으로 재귀적으로 항목을 중첩하는 `children` 속성을 가진 새 객체로 매핑하기 위해 `Array.prototype.map()`을 사용합니다.
5. 두 번째 인수 `id`를 생략하여 객체가 다른 객체에 연결되지 않음을 나타내는 `null`로 기본 설정합니다 (즉, 최상위 객체입니다).
6. 세 번째 인수 `link`를 생략하여 객체를 `id`로 다른 객체에 연결하는 기본 속성으로 `'parent_id'`를 사용합니다.

다음은 코드입니다.

```js
const nest = (items, id = null, link = "parent_id") =>
  items
    .filter((item) => item[link] === id)
    .map((item) => ({ ...item, children: nest(items, item.id, link) }));
```

`nest()` 함수를 사용하려면 `id` 속성과 다른 객체에 연결하는 `parent_id` 속성을 가진 객체 배열을 만듭니다. 그런 다음 `nest()` 함수를 호출하고 배열을 인수로 전달합니다. 이 함수는 `parent_id` 속성을 기반으로 중첩된 새 객체 배열을 반환합니다.

예를 들어:

```js
const comments = [
  { id: 1, parent_id: null },
  { id: 2, parent_id: 1 },
  { id: 3, parent_id: 1 },
  { id: 4, parent_id: 2 },
  { id: 5, parent_id: 4 }
];
const nestedComments = nest(comments);
// [{ id: 1, parent_id: null, children: [...] }]
```
