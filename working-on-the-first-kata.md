# Working on the first kata
Just to get things started let's pick a simple kata to demonstrate the process. Use [Even or Odd Kata](https://www.codewars.com/kata/53da3dbb4a5168369a0000fe) as the first kata to complete these steps with.

If it's not open already, open VS Code. Use `Cmd` + `J` to open the integrated terminal.

## 01. Create branch to solve kata on
You want to isolate the code your writing in a new branch before testing the code and merging it back into the `main` branch.

On a project there are set naming conventions you want to work to when creating a new branch. For this project, we'll use `katalevel-kata-name`.

- Create and change to a new branch locally - `git checkout -b kyu8-even-or-odd`
- Push local branch to remote repo on GitHub `git push -u origin kyu8-even-or-odd` (this sets the local branch to track changes on the remote branch)

> Branch names can't start with a number

## 02. Create Katas directory
You want the structure of the project to make sense to organise your code into logical folders. Part of this is to split the project into `project` and `test` directories.

```
# Add example project structure
```

### 02A. Add to file structure and file for code

- Create a new directory called `katas`
- Within `katas` create a new directory called `kyu8`
- Within `kyu8` create new file called `even_or_odd.py`

> Python has specific [naming conventions](https://visualgit.readthedocs.io/en/latest/pages/naming_convention.html) around naming files (modules).

### 02b. Copy kata code from Codewars

- Copy/Paste code from codewars into the `even_or_odd.py` file.

## 03. Create Test directory

- Create a new directory called `tests`
- Within `tests` create a new directory called `kyu8`
- Within `kyu8` create new file called `test_even_or_odd.py`

> Using `pytest` your test files have to be appended with `test_`. By default `pytest` finds and executes all the files appended with `test_`.

### 03a. Copy test code from Codewars

- Copy/Paste test code from codewars into the `test_even_or_odd.py` file.

## 04. Solve kata then upload solution to Codewars

- Once you're happy with the solution submit it to codewars.
- You can see how other people solved the same problem once submitted so take some time seeing what is considered best practice.

## 05. Testing kata locally

- Make sure your tests are in a `tests` directory and have appended all test files with `test_`. `pytest` searches the project for these so it won't work without this.
- Run `pytest` to run tests.

> Running `pytest` runs all test files. Find a way to filter this to only run the specific test file you're working on.

## 06. Commit changes to remote branch

- Save the files you've worked on.
- Click the `Source Control` icon on the right of the GUI. This shows you the changes you've made to the files.
- Add a commit message - see [commit messages best practice](https://gist.github.com/robertpainsi/b632364184e70900af4ab688decf6f53) for guidance on this.
- Click `Commit`, you might see a popup which asks if you want to stage changes, click yes.
- See screenshots for more information.

<img src="screenshots/04-commit-changes.png" alt="" height="250"/> <img src="screenshots/05-staging-message.png" alt="" height="250"/>

## 07. Push changes

- In the terminal, run `git push`, you may be asked for your passphrase.
- This pushed the changes you commited in the previous step to the remote branch.

## 08. Open a Pull Request on GitHub

- This may seem like overkill for this project but the idea is to get you into the habit of working as you would do on a Code First team. Once you've developed and tested a feature you would open a Pull Request (PR) for a more senior developer to Peer Review before they would merge your change into the code.

<img src="screenshots/.png" alt="" width="400"/>

- Squash merge kata branch to main
- Change working branch to main `git checkout main`
- Pull changes from remote `git pull`