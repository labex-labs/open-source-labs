# 대화형 리베이스 수행하기

여러 명의 개발자와 함께 프로젝트를 진행 중이며, 브랜치에 여러 개의 커밋을 했습니다. 하지만 일부 커밋이 불필요하거나 결합해야 한다는 것을 깨달았습니다. 커밋 기록을 정리하고 더 체계적으로 만들고 싶습니다.

이 랩에서는 `https://github.com/labex-labs/git-playground`의 저장소를 사용해 보겠습니다. 다음 단계를 따르세요:

1. 디렉토리로 이동합니다:
   ```shell
   cd git-playground
   ```
2. 마지막 2 개의 커밋에 대한 대화형 리베이스를 수행합니다:
   ```shell
   git rebase -i HEAD~2
   ```
   대화형 리베이스 파일이 기본 텍스트 편집기에서 열립니다. 커밋 순서와 각 커밋에 대해 수행할 작업 (pick, squash, drop, reword 등) 을 수정할 수 있습니다.
3. "Added file2.txt" 커밋 메시지에서 "pick"을 "squash"로 변경하고, <kbd>Esc</kbd> 키를 누른 다음 <kbd>:wq</kbd> 명령어를 입력한 후 <kbd>Enter</kbd> 키를 눌러 변경 사항을 저장하고 편집기를 종료합니다. 같은 방식으로 커밋 메시지를 "Added file1.txt and file2.txt"로 변경하고 종료합니다.
4. 병합 충돌이 발생하거나 변경을 해야 하는 경우, 준비가 되면 `git rebase --continue`를 사용하여 리베이스를 계속하거나 `git rebase --abort`를 사용하여 중단할 수 있습니다.

`git log`를 실행하면 다음과 같은 결과가 나타납니다:

```shell
[object Object]
```
