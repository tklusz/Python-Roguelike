# Python Roguelike Tutorial 2019 - Part 0.

### Requirements:
* The latest version of Python 3 - [available here.](https://www.python.org/downloads/)
* Libtcodpy -  [available here.](https://github.com/libtcod/python-tcod)
* Libtcodpy documentation can be found [here.](https://python-tcod.readthedocs.io/en/latest/libtcodpy.html)
* A text editor or IDE.
* Basic programming knowledge - methods, variables, loops, if statements, etc.

### Installation
Installing all of our requirements.

#### Python
The installation of Python should be relatively simple. This tutorial is based on the latest version currently available (3.7.2). When installing, be sure to check "add python to path" on Windows, as it will allow you to easily run Python commands through the command line.

![](/docs/images/part-0/python-install.PNG)

If you're using a Linux distribution you should already have Python 3 installed, or should be able to install it using your package manager.

To test if Python was successfully installed, open your command prompt and type "python" (or "python3" on macOS and Linux). You should see the following.

![](/docs/images/part-0/python-console.PNG)

Type ```exit()``` to exit.


#### Libtcodpy
Libtcodpy can be a bit more tricky to setup. After you install Python, open your command prompt or terminal and type the commands located in the README [here (scroll down)](https://github.com/libtcod/python-tcod) based on your operating system.

To assure that libtcodpy was successfully installed, go back to your terminal or command prompt, then type "pip list". You should see a list of packages that are installed, one being tcod.

 ![](/docs/images/part-0/pip-packages.PNG)

Download the latest source code release of libtcodpy [here.](https://github.com/libtcod/python-tcod/releases) We are only downloading the source code for a font file that we need later.


#### Text editor or IDE
Using a smart text editor or IDE while programming can aid you in finding mistakes, spelling errors and remembering class methods just to name a few.

I am using Atom, a smart text editor, for this tutorial. It is similar to Sublime Text, but it's created by the same people behind GitHub. The download page can be found [here.](https://atom.io/)

It is recommended to use Atom for this project as it has useful GitHub and Python integration (such as pushing to GitHub and running Python scripts right from your text editor).  

##### Configuring Atom - Project folder.
Note: If you plan to create a GitHub repository, skip this step for now then come back after reading the "Setting up a GitHub Repository" section.

Once Atom is open for the first time, you should see a welcome screen, which you can close, along with all of the other tabs that open.

Create a folder for your project somewhere, then go back to Atom and go to "File" - "Add Project Folder", then select the folder you created. It should appear on the left side of the screen as seen below.

![](/docs/images/part-0/empty-project-folder.PNG)

Right click the folder in Atom, and click "New Folder". Call the new folder "fonts".

Place the "ariel10x10.png" font from the libtcodpy source code into the new "fonts" folder. This font is located in /fonts/libtcod/ariel10x10.png of the libtcod source code.

This is what your project folder should look like when complete:

![](/docs/images/part-0/adding_fonts.PNG)

Create another folder in your project folder called "src". Right click the src folder in Atom and click "New File". Call this file "engine.py". This is what your project folder should look like now.

![](/docs/images/part-0/project_folder_final.PNG)

After that is complete, the project folder is ready.

##### Configuring Atom - Packages.
Once your project folder is finished, go to the packages setting on the top menu bar, click "Command Palette" then "toggle" (Can also use Ctrl+Shift+P on Windows).

![](/docs/images/part-0/command-pallete.PNG)

Go to "Install Packages and Themes". An "Install Packages" section should appear. Type "python" and install the two packages shown in the screenshot below.

![](/docs/images/part-0/packages.PNG)

After your configuration is complete, you should be able to run Python scripts in your editor using the F5 key.

Once this step is complete (if you're on Windows), you are finished with the required configuration. If you would like to set up a GitHub repository for your project, continue to the "Setting up a GitHub Repository" section.

###### Additional Atom configuration - macOS and Linux.
To properly configure atom-python-run on a Linux distribution or macOS,
click "settings" on the "atom-python-run" package, and set the F5 command to what's shown in the screenshot below (changing python to python3).

![](/docs/images/part-0/package-python3.PNG)

### Setting up a GitHub Repository.
Assuming you already have a GitHub account, go to github.com, then click the plus button on the top-right. Click "new repository." Give your repository a name and description, choose private or public, then create the repository.

If you are using Windows or macOS, it is recommended to use [github desktop](https://desktop.github.com/) to manage your GitHub repository. Open the program after it is installed, sign in, then  click "File" - "New Repository". Select the repository that you created on GitHub.

![](/docs/images/part-0/github-desktop.PNG)

GitHub desktop will create a local folder located in the "local path" section listed at the bottom. Use that folder as your project folder in Atom. As you add or modify code, it will be tracked in Atom in the Git tab (which can be opened by going to "Packages" - "GitHub" - "Toggle GitHub Tab").

Once you have made significant progress, or want to take a break from coding, you can create a commit message, commit, then push to GitHub using either Atom or GitHub Desktop.

Each commit requires a comment, so you can track what you worked on over time, and so others can see a summary what you contributed.

![](/docs/images/part-0/desktop-commit.PNG)

If you are using Atom for your commits, make sure to right-click "stage" each change in the "Unstaged Changes" section before committing.

![](/docs/images/part-0/atom-commit.PNG)

After you commit, you need to push your commit up to GitHub. You can do this in Atom by clicking the "Push" button on the bottom right.

![](/docs/images/part-0/atom-push.PNG)

On GitHub desktop, click the "Push Origin" button on the top after creating your commit.

![](/docs/images/part-0/github-push.PNG)

After you push your commit to GitHub, you should be able to see your changes on your repository.

If you're interested in more complex GitHub features such as branching and pull requests there is a good tutorial [here](https://guides.github.com/activities/hello-world/).
