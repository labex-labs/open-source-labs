# HTML 구조 생성

이제 프로젝트 파일을 이해했으므로 체커보드 패턴에 대한 HTML 구조를 만들어 보겠습니다.

1. 편집기에서 `index.html` 파일을 다시 엽니다.

2. 체커보드 패턴을 위한 컨테이너 요소를 추가해야 합니다. `<body>` 태그 내에서 주석을 "checkerboard" 클래스를 가진 `<div>` 요소로 바꿉니다.

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Checkerboard Pattern</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <div class="checkerboard"></div>
  </body>
</html>
```

3. Ctrl+S 를 누르거나 파일 > 저장을 클릭하여 `index.html` 파일을 저장합니다.

4. 이제 체커보드의 치수를 정의하기 위해 몇 가지 기본 CSS 를 추가해 보겠습니다. `style.css` 파일을 열고 다음 코드를 추가합니다.

```css
.checkerboard {
  width: 240px;
  height: 240px;
  background-color: #fff;
}
```

이 CSS 코드는 다음을 수행합니다.

- 체커보드의 너비와 높이를 240 픽셀로 설정합니다.
- 배경색을 흰색 (#fff) 으로 설정합니다.

5. `style.css` 파일을 저장합니다.

6. 변경 사항을 확인하려면 **Web 8080** 탭을 새로 고칩니다.

이제 너비와 높이가 240 픽셀인 흰색 사각형이 표시됩니다. 이것이 체커보드 패턴을 위한 캔버스가 됩니다.
