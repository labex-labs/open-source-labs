# HTML 구조 이해

애니메이션을 만들기 전에, 우리가 작업할 HTML 구조를 이해해야 합니다. 이 단계에서는 제공된 HTML 파일을 검토하고 필요한 수정 사항을 적용합니다.

1. 편집기에서 `index.html` 파일을 엽니다.

2. 파일이 비어 있거나 없는 경우, 다음 내용으로 파일을 생성합니다:

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Zoom In Zoom Out Animation</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <h1>CSS Animation Demo</h1>
    <p>This box demonstrates a zoom in zoom out animation:</p>

    <div class="zoom-in-out-box"></div>
  </body>
</html>
```

3. 이 HTML 이 무엇을 하는지 이해해 봅시다:
   - 제목과 viewport (뷰포트) 설정을 갖춘 표준 HTML 문서 구조가 있습니다.
   - `style.css`라는 외부 CSS 파일에 연결합니다.
   - 데모를 설명하기 위해 제목과 단락을 포함합니다.
   - 가장 중요한 것은, 애니메이션될 클래스 `zoom-in-out-box`를 가진 `<div>` 요소가 있다는 것입니다.

4. 변경 사항이 있는 경우 `index.html` 파일을 저장합니다.

이 div 요소는 애니메이션을 생성하기 위한 캔버스가 될 것입니다. 다음 단계에서는 CSS 를 사용하여 이 요소의 스타일을 지정합니다.
