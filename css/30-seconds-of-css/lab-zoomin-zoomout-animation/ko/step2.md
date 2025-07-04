# 기본 CSS 스타일 지정

이제 HTML 구조가 준비되었으므로, 애니메이션 요소에 대한 기본 CSS 스타일을 만들어 보겠습니다.

1. 편집기에서 `style.css` 파일을 엽니다.

2. 파일이 비어 있거나 없는 경우, 다음 내용으로 파일을 생성합니다:

```css
body {
  font-family: Arial, sans-serif;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

h1 {
  color: #333;
}

.zoom-in-out-box {
  margin: 24px;
  width: 50px;
  height: 50px;
  background: #f50057;
}
```

3. 이 CSS 가 무엇을 하는지 이해해 봅시다:
   - 페이지에 대한 몇 가지 기본 스타일 (글꼴, 너비 및 여백) 을 설정합니다.
   - 제목을 어두운 회색으로 스타일링합니다.
   - 애니메이션 요소 `.zoom-in-out-box`에 대해 다음을 수행합니다:
     - 주변에 24px 의 여백을 추가합니다.
     - 너비와 높이를 50px 로 설정합니다.
     - 생생한 분홍색 배경색을 지정합니다.

4. 이러한 변경 사항을 적용한 후 `style.css` 파일을 저장합니다.

5. 진행 상황을 확인하려면 VSCode 의 오른쪽 하단 모서리에 있는 "Go Live" 버튼을 클릭합니다. 이렇게 하면 포트 8080 에서 웹 서버가 시작됩니다. 그런 다음 **Web 8080** 탭을 새로 고쳐 스타일이 지정된 상자를 확인합니다.

이제 웹 페이지에 작은 분홍색 사각형이 표시됩니다. 이 사각형은 다음 단계에서 애니메이션을 적용할 요소입니다.
