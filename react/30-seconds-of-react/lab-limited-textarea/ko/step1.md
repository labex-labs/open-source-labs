# 문자 제한이 있는 Textarea

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

다음은 코드입니다:

```jsx
const LimitedTextarea = ({ rows, cols, value, limit }) => {
  const [content, setContent] = React.useState(value.slice(0, limit));

  const setFormattedContent = React.useCallback(
    (text) => {
      setContent(text.slice(0, limit));
    },
    [limit]
  );

  return (
    <>
      <textarea
        rows={rows}
        cols={cols}
        onChange={(event) => setFormattedContent(event.target.value)}
        value={content}
      />
      <p>
        {content.length}/{limit}
      </p>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <LimitedTextarea limit={32} value="Hello!" />
);
```

이 코드에서 우리는 다음을 수행했습니다:

- 코드 각 부분이 수행하는 작업에 대한 보다 간결한 개요를 제공하기 위해 주석을 단순화했습니다.
- 불필요한 코드 주석을 제거했습니다.
- `useCallback` 종속성 배열에서 `setContent` 함수를 제거했습니다. (필요하지 않기 때문입니다.)
- 일관성을 위해 `useCallback` 함수의 `text` 인수에 괄호를 추가했습니다.
- 간결성을 위해 `onChange` 이벤트 핸들러에 화살표 함수를 사용했습니다.

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
