# 요약

Git 에서 원격 브랜치 이름을 변경하는 것은 로컬과 원격 모두에서 브랜치 이름을 변경하는 것을 포함합니다. `git branch -m <old-name> <new-name>` 명령을 사용하여 로컬 브랜치의 이름을 변경하고, `git push origin --delete <old-name>` 및 `git push origin -u <new-name>` 명령을 사용하여 이전 원격 브랜치를 삭제하고 새 원격 브랜치를 설정할 수 있습니다.
