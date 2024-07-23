# Project Setup

## Overview
1. Create accounts
2. Create project (remote)
3. Set up SSH key
4. Create project (local)
5. Set `git config` for project
6. Open project in VS Code

## Create Accounts

1. Create [GitHub account](https://github.com/)
2. Create [Codewars account](https://codewars.com/) - you can sign up to this by using you GitHub account if you want.

## Create Project (remote)

3. Create a new Repository (repo) in GitHub - see screen shot

<img src="screenshots/01-new-repo.png" alt="" width="400"/>

4. Fill in repo details - see screen shot
- Make sure the Owner is your GitHub profile.
- Repository name could be `codewars-dcdp` (Or something else that makes sense to you).
- Tick 'Add a README file'
- Add a `.gitignore` for `Python`
- Click 'Create Repository'

> [More information](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files) about `.gitignore` files.

<img src="screenshots/02-repo-options.png" alt="" width="400"/>

## Set up SSH key

> These next steps might seem a bit complicated so reach out if you need help with this next part. Unfortunately, there's no alternative to this.

### Essential Setup:

5. From the terminal run `ssh-keygen -t ed25519 -C "your_email@example.com"`. Replace with the email address you used for GitHub.
6. When you're prompted to "Enter a file in which to save the key", you can press `Enter` to accept the default file location.
7. At the prompt, type a secure passphrase and press `Enter`.

> This passphrase is important and you will need to remember it. If you forget it you will need to create a new SSH to replace this one.

8. Copy the SSH key using the command `pbcopy < ~/.ssh/id_ed25519.pub`

### Advanced Setup (you can skip this if you want):

Follow the instructions to [add your SSH key to the ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent). Doing this means that you don't need to enter your passphrase each time you interact with GitHub from the command line. You will understand this step more by working on this project so skips this for now if you're unsure.

### Useful documentation if you get stuck:

- For information about generating SSH keys, see [Generating a new SSH key and adding it to the ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key)

- For more information about Adding SSH keys to GitHub [Adding a new SSH key to your account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account#adding-a-new-ssh-key-to-your-account)

- For more information about working with passphrases, see [Working with SSH key passphrases](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/working-with-ssh-key-passphrases)

## Create project (local)

9. Now you can use SSH to clone a repo from GitHub. Click `Code`, `SSH`, `Copy URL to clipboard` - see screenshot

<img src="screenshots/03-clone-repo.png" alt="" width="400"/>

10. Open terminal.

11. Navigate to a location in the file system where you would like this project to live. For example, if you want the project to be located `/Documents/cpd` you can enter the following:

```sh
cd Documents
mkdir cpd
cd cpd
```

> For more information about using the command line see [Basic Linux Commands](https://www.geeksforgeeks.org/basic-linux-commands/).

12. Using terminal, clone the repo into the directory using `git clone <the URL you copied from GitHub>`. Replace `<the URL you copied from GitHub>` with the URL.

13. Navigate into project using `cd codewars-dcdp` (or whatever name you gave the project).

## Set `git config` for project

14. As you are using a work laptop with your personal GitHub account you will want to override the global git config settings in this project. This is so you don't accidentally make a commit to this project with your work account or make a commit on a work project with your personal account.

15. Make sure you are in the correct directory (you should be if you have followed these steps in order). Use the command `pwd`. This should show the current working directory, this should match the location where you project lives.

16. In terminal, use `git config user.name "github-username"` then `git config user.email "github@email.com"`. The name and email should be the ones you used to set up your GitHub account with.

## Open project in VS Code

17. Open the project from terminal using `code .` (Make sure to include the `.`)

This leaves you in a good place to start working on the project. Continue to next steps.

---