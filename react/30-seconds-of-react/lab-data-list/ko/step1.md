# 데이터 목록 (Data List)

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

이 함수는 원시 값의 배열에서 항목 목록을 렌더링합니다. `isOrdered` prop 의 값에 따라 정렬된 목록 또는 정렬되지 않은 목록을 조건부로 렌더링하는 데 사용할 수 있습니다. `data` 배열의 각 항목을 렌더링하기 위해 `Array.prototype.map()`을 사용하여 각 항목에 대해 고유한 `key`를 가진 `<li>` 요소를 생성합니다.

```jsx
const DataList = ({ data, isOrdered = false }) => {
  const list = data.map((value, index) => (
    <li key={`${index}_${value}`}>{value}</li>
  ));

  return isOrdered ? <ol>{list}</ol> : <ul>{list}</ul>;
};
```

다음은 이 컴포넌트를 사용하는 방법의 예입니다.

```jsx
const names = ["John", "Paul", "Mary"];
ReactDOM.createRoot(document.getElementById("root")).render(
  <>
    <DataList data={names} />
    <DataList data={names} isOrdered={true} />
  </>
);
```

이 예제에서는 이름 배열을 `DataList` 컴포넌트에 전달하고 두 번 렌더링합니다. 처음에는 정렬되지 않은 목록을 렌더링하고, 두 번째에는 정렬된 목록을 렌더링합니다.

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
