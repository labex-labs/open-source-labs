# Setting up the Development Environment

Before you start, you'll need to install Node.js and npm (Node Package Manager). Angular requires Node.js version 10.13 or later.

1. **Install Node.js and npm:**
   Visit [Node.js website](https://nodejs.org/) and download the installer for your operating system. This will also install npm.

   Node v16.14 is already installed in the environment for us, use node -v to check the version of Node in the environment, if it is not v16.14, use the following command to install it.

   ```bash
   wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash
   nvm install 16.14
   nvm use 16.14
   nvm alias default 16.14
   ```

2. **Install Angular CLI:**
   Angular CLI (Command Line Interface) is a tool to initialize, develop, scaffold, and maintain Angular applications. Install it globally using npm:

```sh
npm install -g @angular/cli
```

If you get an error during the installation process, add `sudo`.
