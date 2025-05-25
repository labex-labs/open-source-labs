# 리스트 렌더링

> React 프로젝트는 이미 VM 에 제공되어 있습니다. 일반적으로 `App.js`에 코드만 추가하면 됩니다.

다음 명령을 사용하여 종속성을 설치하십시오.

```bash
npm i
```

컴포넌트 리스트를 렌더링하기 위해 for 루프 및 배열 `map()` 함수와 같은 JavaScript 기능을 사용합니다.

예를 들어, 제품 배열이 있다고 가정해 보겠습니다.

```js
const products = [
  { title: "Cabbage", id: 1 },
  { title: "Garlic", id: 2 },
  { title: "Apple", id: 3 }
];
```

컴포넌트 내부에서 `map()` 함수를 사용하여 제품 배열을 `<li>` 항목 배열로 변환합니다.

```js
const listItems = products.map((product) => (
  <li key={product.id}>{product.title}</li>
));

return <ul>{listItems}</ul>;
```

`<li>`에 key 속성이 있는 것을 확인하십시오. 리스트의 각 항목에 대해 형제 항목 중에서 해당 항목을 고유하게 식별하는 문자열 또는 숫자를 전달해야 합니다. 일반적으로 key 는 데이터베이스 ID 와 같은 데이터에서 가져와야 합니다. React 는 나중에 항목을 삽입, 삭제 또는 재정렬하는 경우 key 를 사용하여 어떤 일이 발생했는지 파악합니다.

```js
// App.js
const products = [
  { title: "Cabbage", isFruit: false, id: 1 },
  { title: "Garlic", isFruit: false, id: 2 },
  { title: "Apple", isFruit: true, id: 3 }
];

export default function ShoppingList() {
  const listItems = products.map((product) => (
    <li
      key={product.id}
      style={{
        color: product.isFruit ? "magenta" : "darkgreen"
      }}
    >
      {product.title}
    </li>
  ));

  return <ul>{listItems}</ul>;
}
```

프로젝트를 실행하려면 다음 명령을 사용하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.

```bash
npm start
```
