# Remote URL 변경

GitHub 에서 리포지토리를 clone 하고 몇 가지 변경 사항을 적용했습니다. 하지만 이제 remote 리포지토리의 URL 을 변경해야 한다는 것을 깨달았습니다. 이는 원래 리포지토리가 다른 위치로 이동했거나, 변경 사항을 다른 remote 리포지토리에 push 하려는 경우일 수 있습니다. 여러분의 과제는 Git 명령어를 사용하여 리포지토리의 remote URL 을 변경하는 것입니다.

`https://github.com/labex-labs/git-playground` 리포지토리를 로컬 머신에 clone 해야 합니다. 리포지토리의 remote URL 을 `https://github.com/your-username/git-playground`로 변경하려면 다음 단계를 따르세요.

1. 터미널 또는 명령 프롬프트를 열고, 리포지토리를 clone 한 후 로컬 리포지토리로 이동합니다.
   ```
   git clone https://github.com/labex-labs/git-playground
   cd git-playground
   ```
2. 현재 remote URL 을 확인하려면 다음 명령어를 사용합니다.
   ```
   git remote -v
   ```
3. remote URL 을 새 URL 로 변경하려면 다음 명령어를 사용합니다.
   ```
   git remote set-url origin https://github.com/your-username/git-playground
   ```
4. remote URL 이 변경되었는지 확인하려면 다음 명령어를 사용합니다.
   ```
   git remote -v
   ```

출력 결과는 이전 URL 대신 새 URL 을 표시해야 합니다.

![Updated remote URL output](../assets/challenge-change-remote-url-step1-1.png)
