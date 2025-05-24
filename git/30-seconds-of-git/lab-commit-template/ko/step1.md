# 커밋 메시지 템플릿 추가

커밋 메시지 템플릿이 없으면 개발자는 "버그 수정" 또는 "코드 업데이트"와 같이 모호하거나 정보가 부족한 커밋 메시지를 작성하려는 유혹을 받을 수 있습니다. 이는 다른 사람이 변경 사항의 목적을 이해하기 어렵게 만들고, 혼란이나 실수를 초래할 수 있습니다. 커밋 메시지 템플릿을 설정하면 개발자는 더 자세하고 유익한 커밋 메시지를 제공하도록 권장되며, 이는 협업과 생산성을 향상시킬 수 있습니다.

이 랩에서는 `https://github.com/labex-labs/git-playground`의 저장소를 사용해 보겠습니다. 이 저장소에 대한 커밋 메시지 템플릿을 설정하려면 다음 단계를 따르세요.

1. `git clone https://github.com/labex-labs/git-playground` 명령을 사용하여 저장소를 로컬 머신에 복제합니다.
2. `cd git-playground` 명령을 사용하여 저장소 디렉토리로 이동하고, `git config --global user.name "your-username"` 및 `git config --global user.email "your-email"` 명령을 사용하여 GitHub 계정을 구성합니다.
3. `vim commit-template` 명령을 사용하여 저장소 디렉토리에 `commit-template`라는 새 파일을 생성합니다.
4. 텍스트 편집기에서 `commit-template` 파일을 열고 다음 줄을 추가합니다.

```shell
# <type>: <subject>

# <body>

# <footer>

#This creates a template with three sections, where "<type>" indicates the type of submission, such as "feat" or "fix", "<subject>" is a short #summary describing the content of the submission, "<body>" is a more detailed description, and "<footer>" can contain other metadata, such as the #associated issue number or other comments.
```

5. <kbd>Esc</kbd> 키를 누르고 <kbd>:wq</kbd> 명령을 입력한 다음 <kbd>Enter</kbd> 키를 눌러 변경 사항을 저장하고 `commit-template` 파일 편집기를 종료합니다.
6. `git add commit-template` 명령을 사용하여 `commit-template` 파일을 스테이징 영역에 추가합니다.
7. `git config commit.template commit-template` 명령을 사용하여 `commit-template` 파일을 저장소의 커밋 메시지 템플릿으로 설정합니다.
8. `git commit` 명령을 사용하여 커밋 메시지 편집기를 열고, 커밋 메시지 편집기에 4 단계에서 생성한 커밋 메시지 템플릿이 포함되어 있는지 확인합니다.
9. <kbd>Esc</kbd> 키를 누르고 <kbd>:q</kbd> 명령을 입력한 다음 <kbd>Enter</kbd> 키를 눌러 커밋 메시지 편집기를 종료합니다.
