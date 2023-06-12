# Fix the bug

Replace the `> ` with `>=` in the conditional on the next line:

![Image of VS Code line 24 to fix](../images/fixing-line.png "Image of Visual Studio Code line 24 to fix")

Now save the file. A second or two later, you should see the debugger detach and then reattach (the yellow line highlighting the breakpoint will disappear and reappear). This is because several things have just happened:

- Upon saving the file, Docker detected the filesystem change event and proxied it through to the container.
- nodemon detected the event and restarted the application. You can confirm this by looking at your terminal: there should be a line that reads “restarting due to changes…”
- Finally, VSCode detected that the remote debugger had gone away and reattached.

The debugger is now attached again. However, your browser tab might have errored out – go refresh it if so.

You can now step through the debugger once again and see that the lines cycle properly – no more `undefined`.

![Animated image of VS Code hitting the breakpoint with line fixed](../images/attach.png "Animated image of Visual Studio Code hitting the breakpoint with line fixed")

Remove the breakpoint and detach the debugger by clicking the stop button. Go back to the browser window and enjoy the updated experience.

![Animated image of browser without error](../images/attach.png "Animated image of browser without error")

And that's it, you're done!

{:.quiz}
True or false: You have to restart a container after you make changes to the code or they won't be reflected in the application

- ( ) True
- (x) False

{:.quiz}
True or false: Debugging a NodeJS app running in a container requires a special plugin for the IDE

- ( ) True
- (x) False
