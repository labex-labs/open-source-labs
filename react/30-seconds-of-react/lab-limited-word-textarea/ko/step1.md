# 단어 제한이 있는 Textarea

> `index.html`과 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js`와 `style.css`에만 코드를 추가하면 됩니다.

```jsx
// 단어 제한이 있는 textarea 컴포넌트를 렌더링합니다.
const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
  const [{ content, wordCount }, setContent] = React.useState({
    content: value,
    wordCount: 0
  });

  // 입력 텍스트의 형식을 지정하는 메모이제이션된 함수를 생성합니다.
  const setFormattedContent = React.useCallback(
    (text) => {
      const words = text.split(" ").filter(Boolean);
      const truncated = words.slice(0, limit).join(" ");
      setContent({
        content: words.length > limit ? truncated : text,
        wordCount: words.length > limit ? limit : words.length
      });
    },
    [limit, setContent]
  );

  // content 의 초기 값에 setFormattedContent 를 호출합니다.
  React.useEffect(() => {
    setFormattedContent(content);
  }, []);

  return (
    <>
      <textarea
        rows={rows}
        cols={cols}
        value={content}
        onChange={(event) => setFormattedContent(event.target.value)}
      />
      <p>
        {wordCount}/{limit}
      </p>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <LimitedWordTextarea limit={5} value="Hello there!" />
);
```

변경 사항:

- 코드의 각 부분이 무엇을 하는지 설명하는 주석을 추가했습니다.
- `setFormattedContent`의 로직을 간소화하여 더 간결하게 만들었습니다.
- 가독성을 높이기 위해 `setContent` 함수를 함수 호출의 끝으로 이동했습니다.
- 일관성을 위해 `<textarea>` 컴포넌트의 props 순서를 재정렬했습니다.
- 불필요한 공백과 줄 바꿈을 제거했습니다.

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
