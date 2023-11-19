# Setting up the Development Environment

Before you start, you'll need to install Node.js and npm (Node Package Manager). Angular requires Node.js version 10.13 or later.

1. **Install Node.js and npm:**
   Angular requires Node version above 18.13, so first use node -v to check the node version, if it is lower than 18.13, please use the following command to change the node version.

   ```bash
   nvm install 18.13
   nvm use 18.13
   nvm alias default 18.13
   ```

2. **Install Angular CLI:**
   Angular CLI (Command Line Interface) is a tool to initialize, develop, scaffold, and maintain Angular applications. Install it globally using npm:

```sh
npm install -g @angular/cli
```

If you get an error during the installation process, add `sudo`.
