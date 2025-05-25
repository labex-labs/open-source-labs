# 데이터 테이블

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

두 개의 열, `ID`와 `Value`를 가진 테이블 요소를 생성합니다. 여기서 각 행은 기본형 값의 배열에서 동적으로 생성됩니다.

이를 위해 `Array.prototype.map()` 메서드를 사용하여 입력 `data` 배열의 각 항목을 적절한 `key`를 가진 `<tr>` 요소로 나타내는 JSX 요소의 새 배열을 생성합니다. 각 `<tr>` 내부에, 행의 인덱스와 값을 각각 표시하기 위해 두 개의 `<td>` 요소를 추가합니다.

다음은 예시 구현입니다.

```jsx
const DataTable = ({ data }) => {
  return (
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Value</th>
        </tr>
      </thead>
      <tbody>
        {data.map((val, i) => (
          <tr key={`${i}_${val}`}>
            <td>{i}</td>
            <td>{val}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};
```

예를 들어, 사람들의 이름 배열과 함께 이 컴포넌트를 사용하려면 다음과 같이 호출할 수 있습니다.

```jsx
const people = ["John", "Jesse"];
ReactDOM.createRoot(document.getElementById("root")).render(
  <DataTable data={people} />
);
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
