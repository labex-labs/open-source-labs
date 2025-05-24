# Git Stash 삭제하기

`https://github.com/labex-labs/git-playground`라는 이름의 Git 저장소가 있습니다. `git stash save "my stash"` 명령을 사용하여 stash 를 생성했습니다. 이제 더 이상 필요하지 않으므로 이 stash 를 삭제하려고 합니다.

1. `cd git-playground` 명령을 사용하여 저장소 디렉토리로 이동합니다.
2. `git stash list` 명령을 사용하여 모든 stash 를 나열합니다. 방금 생성한 stash 가 표시되어야 합니다.
3. `git stash drop stash@{0}` 명령을 사용하여 stash 를 삭제합니다.
4. `git stash list` 명령을 사용하여 다시 모든 stash 를 나열합니다.

방금 삭제한 stash 는 더 이상 존재하지 않아야 합니다.
