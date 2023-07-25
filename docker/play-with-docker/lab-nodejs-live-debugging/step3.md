# Start debugging

Open up the app directory in VSCode. Head over to the debugger by clicking the bug icon in the left-hand sidebar.

![Image of VS Code with debugger icon highlighted](../images/debugger-icon.png "Image of Visual Studio Code with debugger icon highlighted")

Create a boilerplate debugger config by clicking the gear icon and selecting “Node.js” in the dropdown.

![Image of VS Code with gear icon highlighted](../images/gear-icon.png "Image of Visual Studio Code with gear icon highlighted")

![Image of VS Code dropdown list](../images/dropdown.png "Image of Visual Studio Code dropdown list")

A JSON file will be created and displayed. Replace its contents with the following:

```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Attach",
            "type": "node",
            "request": "attach",
            "port": 5858,
            "address": "localhost",
            "restart": true,
            "sourceMaps": false,
            "outDir": null,
            "localRoot": "${workspaceRoot}",
            "remoteRoot": "/code"
        }
    ]
}
```

There are three important changes here:

- The whole “Launch” config has been deleted – you’re using Compose to launch the app, not VSCode, so it’s unnecessary.
- `restart` is set to true, so that the debugger re-attaches when the app restarts.
- `remoteRoot` is set to the path of the code directory inside the container, because it’s almost certainly different than the path to the code on your machine.

With the “Attach” config selected, click the “play” button to start the debugger.
![Image of VS Code attach icon](../images/attach.png "Image of Visual Studio Code attach icon")

Now go back to app.js and find the line that reads `lineIndex += 1` line, just after we initialize the `message` variable. Set a breakpoint by clicking in the gutter, just to the left of the line number.
![Image of VS Code breakpoint](../images/breakpoint.png "Image of Visual Studio Code breakpoint")

If your browser window is still open and refreshing, in a second or two you should see it hit the breakpoint. If not, go back and refresh it – VSCode will pop back to the front as soon as the debugger hits it.

Hit the Play button at the top to resume code execution. It’ll hit the breakpoint every time the browser refreshes, which is every 2 seconds. You can see it cycling through the lines, and then the bug shows up – right after the last line, message gets set to undefined.
![Animated image of VS Code hititng breakpoint](../images/hitting-breakpoint.gif "Animated image of VS Code hititng breakpoint")

The reason becomes clear if you open up the “Closure” section under “VARIABLES”: `lineIndex` has incremented to 4 – the length of the `LINES` array – when it should have been reset after getting to 3. We’ve got an off-by-one error.
![Image of VS Code lineIndex value](../images/variables.png "Image of Visual Studio Code lineIndex value")
