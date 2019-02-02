# Python Roguelike Tutorial 2019 - Part 0.

### Requirements:
* The latest version of Python 3 - [available here.](https://www.python.org/downloads/)
* Libtcodpy -  [available here.](https://github.com/libtcod/python-tcod)
* Libtcodpy documentation can be found [here.](https://python-tcod.readthedocs.io/en/latest/libtcodpy.html)
* A text editor or IDE (Covered in part 0).
* Basic programming knowledge - methods, variables, loops, if statements, etc.

### Installation
Installing all of our requirements.

#### Python
The installation of Python should be relatively simple. This tutorial is based on the current latest version (3.7.2). When installing, be sure to check "add python to path" if you're using Windows, as it will allow you to easily run Python commands through the command line.

![](/docs/images/part-0/python-install.PNG)

If you're using a Linux distribution you should already have Python3 installed, or should be able to install it using your package manager.

To test if Python was successfully installed, open your command prompt or terminal and type "python". You should see the following.

![](/docs/images/part-0/python-console.PNG)

Type ```exit()``` to exit.


#### Libtcodpy
Libtcodpy can be a bit more tricky to setup. After you install Python, open your command prompt or terminal and type the commands located in the README [here (scroll down)](https://github.com/libtcod/python-tcod) based on your operating system.

To assure that libtcodpy was successfully installed, go back to your terminal or command prompt, then type "pip list". You should see a list of packages that are installed, one being tcod.

 ![](/docs/images/part-0/pip-packages.PNG)

Download the latest source code release of libtcodpy [here.](https://github.com/libtcod/python-tcod/releases) We are only downloading the source code for a font file that we need later.


#### Text editor or IDE
I am using Atom, a "smart" text editor, for this tutorial. It is similar to Sublime Text, but it's created by the same people behind GitHub. The download page can be found [here.](https://atom.io/)

It is recommended to use Atom for this project as it has simple GitHub and Python integration.  

##### Configuring Atom - Project folder.
Once Atom is open for the first time, you should see a welcome screen, which you can close, along with all of the other tabs that open.

Create a folder for your project somewhere, then go back to Atom and go to "File" - "Add Project Folder", then select the folder you created. It should appear on the left side of the screen as seen below.

![](/docs/images/part-0/empty-project-folder.PNG)

##### Configuring Atom - Packages.
Once you have Atom installed, go to the packages setting on the top menu bar, click "Command Palette" then "toggle" (Can also use Ctrl+Shift+P on Windows).

![](/docs/images/part-0/command-pallete.PNG)

Type "Install Packages and Themes". An "Install Packages" section should appear. Type "python" and install the two packages shown in the screenshot below.

![](/docs/images/part-0/packages.PNG)

###### Additional Atom configuration - Linux only.
Do the following only if you're on a Linux distribution (may be required for macOS distributions as well).

After your packages are installed, click "settings" on the "atom-python-run" package, and set the f5 command to what's shown in the screenshot below (changing python to python3).

![](/docs/images/part-0/package-python3.PNG)

After your configuration is complete, you should be able to run python scripts in your editor using the f5 key.

Once this step is complete, you are finished with the required configuration. If you would like to set up a GitHub repository for your project, continue to the following section.

### Setting up a GitHub repository.
Assuming you already have a GitHub account, go to github.com, then click the plus button on the top-right. Click "new repository." Give your repository a name and description, choose private or public, then create the repository.

If you are using Windows or macOS, it is recommended to use [github desktop](https://desktop.github.com/) to manage your GitHub repository. Open the program after it is installed, sign in, then add a new repository. Select the repository that you created.

![](/docs/images/part-0/github-desktop.PNG)

GitHub desktop will create a local folder located in the "local path" section listed at the bottom. Use that folder as your project folder in Atom. As you add or modify code, it will be tracked in Atom in the Git tab (which can be opened by going to "Packages" - "GitHub" - "Toggle GitHub Tab").

Once you have made significant progress, or want to take a break from coding, you can create a commit message, commit, then push to GitHub using either Atom or GitHub Desktop.

Each commit requires a comment, so you can track what you worked on over time, and so others can see a summary what you contributed.

![](/docs/images/part-0/desktop-commit.PNG)

If you are using Atom for your commits, make sure to right-click "stage" each change in the "Unstaged Changes" section before comitting.

![](/docs/images/part-0/atom-commit.PNG)
