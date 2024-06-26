# Dotfiles for Work Mac

My dev setup and workflow for intel macOS.

![Terminal Image](/assets/terminal.png "My terminal image")

My setup and tools:

- Terminal: [Kitty](https://github.com/kovidgoyal/kitty), previously [Alacritty](https://github.com/alacritty/alacritty)
- Prompt: [Starship](https://starship.rs/)
- Shell: [Fish](https://fishshell.com/)
- Editor: [VS Code](https://code.visualstudio.com/) and [Neovim](https://github.com/neovim/neovim)
- Fonts: [Nerd Fonts](https://www.nerdfonts.com/)
- Dotfiles Management: [GNU Stow](https://www.gnu.org/software/stow/)

## Installation

I use [vscode](https://code.visualstudio.com/docs/setup/mac) as my main editor.

Once you install vscode, run this command to install extensions: `just vsc-ext`

### Clone this repo and run these commands to create my dev workflow

My recommendation is clone this repo into `$HOME/.dotfiles` like this

```sh
# install xcode cli tools: need git installed
xcode-select --install

# clone repo to dotfiles dir
git clone git@github.com:joefitzy/dotfiles.git $HOME/.dotfiles

# Move into dotfiles dir
cd $HOME/.dotfiles

# install homebrew
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# install packages from brewfile
brew update && brew install just
just brewinstall

# install virtualenv
pipx install virtualenv

# use gnu stow to manage symlinks for dotfiles
# must be in $HOME/.dotfiles directory
stow .
```

## Troubleshooting

### Alacritty

You might need to make a symlink to your fish install like this:

```sh
ln -s <current_fish_locaation> /usr/local/bin/fish
```
