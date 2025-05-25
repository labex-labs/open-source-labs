# 객체 테이블 뷰

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

이 컴포넌트는 객체 배열과 속성 이름 목록에서 동적으로 생성된 행으로 테이블을 렌더링합니다. 이를 위해 다음을 수행합니다.

- `Object.keys()`, `Array.prototype.filter()`, `Array.prototype.includes()`, 그리고 `Array.prototype.reduce()`를 사용하여 `propertyNames`에 지정된 키를 가진 모든 객체를 포함하는 `filteredData` 배열을 생성합니다.
- `propertyNames`의 값 수와 동일한 열 집합을 가진 `<table>` 요소를 렌더링합니다.
- `Array.prototype.map()`을 사용하여 `propertyNames` 배열의 각 값을 `<th>` 요소로 렌더링합니다.
- `Array.prototype.map()`을 사용하여 `filteredData` 배열의 각 객체를 객체의 각 키에 대한 `<td>`를 포함하는 `<tr>` 요소로 렌더링합니다.
- 이 컴포넌트는 중첩된 객체와 함께 작동하지 않으며 `propertyNames`에 지정된 속성 내에 중첩된 객체가 있는 경우 작동하지 않습니다.

다음은 코드입니다.

```jsx
const MappedTable = ({ data, propertyNames }) => {
  const filteredData = data.map((obj) =>
    Object.keys(obj)
      .filter((key) => propertyNames.includes(key))
      .reduce((acc, key) => ({ ...acc, [key]: obj[key] }), {})
  );

  return (
    <table>
      <thead>
        <tr>
          {propertyNames.map((name) => (
            <th key={`header-${name}`}>{name}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {filteredData.map((obj, i) => (
          <tr key={`row-${i}`}>
            {propertyNames.map((name) => (
              <td key={`cell-${i}-${name}`}>{obj[name]}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
};
```

객체 배열과 속성 이름 목록을 전달하여 컴포넌트를 사용할 수 있습니다.

```jsx
const people = [
  { name: "John", surname: "Smith", age: 42 },
  { name: "Adam", surname: "Smith", gender: "male" }
];
const propertyNames = ["name", "surname", "age"];

ReactDOM.render(
  <MappedTable data={people} propertyNames={propertyNames} />,
  document.getElementById("root")
);
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
