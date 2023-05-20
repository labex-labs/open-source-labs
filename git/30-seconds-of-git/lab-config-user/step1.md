# Configure Git User Information

You have just started working on a new project and want to configure your user information for Git. You want to make sure that your name and email address are associated with any changes you make to the repository.

For this lab, we will be using the Git repository named `https://github.com/labex-labs/git-playground`. Follow these steps to configure your user information for this repository:

1. Clone the repository using the following command: 
```
git clone https://github.com/labex-labs/git-playground.git
```
2. Navigate to the cloned repository using the following command: 
```
cd git-playground
```
3. Use the `git config` command to set your user information for the repository. For example, if your email address is `jane.doe@example.com` and your name is `Jane Doe`, you would use the following commands:

```
git config user.email "jane.doe@example.com"
git config user.name "Jane Doe"
```
4. Verify that your user information has been set correctly by using the following command: `git config --list`. You should see your email address and name listed under the `user.email` and `user.name` keys, respectively.

This is the result after completing the lab:

![<result>](assets/challenge-config-user-step1-1.png)