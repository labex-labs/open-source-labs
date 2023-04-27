# Clone Missing Submodules

You are working on a project that contains submodules. When you clone the project, the submodules are not automatically cloned. This causes issues when trying to build or run the project. You need to clone the missing submodules and checkout the correct commits.

For this challenge, we will use the Git repository named `https://github.com/labex-labs/git-playground`. This repository contains submodules that are not automatically cloned when you clone the repository.

To clone the missing submodules and checkout the correct commits, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/labex-labs/git-playground.git
   ```
2. Change into the repository directory:
   ```
   cd git-playground
   ```
3. Initialize the submodules:
   ```
   git submodule update --init --recursive
   ```
4. Checkout the correct commits for the submodules:
   ```
   git submodule foreach git checkout master
   ```
