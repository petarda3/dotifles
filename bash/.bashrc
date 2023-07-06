#~/.bashrc
# If not running interactively, don't do anything 
[[ $- != *i* ]] && return

# Extract function
ex ()
{
    if [ -f "$1" ] ; then
        case $1 in
          *.tar.bz2)   tar xjf $1   ;;
          *.tar.gz)    tar xzf $1   ;;
          *.bz2)       bunzip2 $1   ;;
          *.rar)       unrar x $1   ;;
          *.gz)        gunzip $1    ;;
          *.tar)       tar xf $1    ;;
          *.tbz2)      tar xjf $1   ;;
          *.tgz)       tar xzf $1   ;;
          *.zip)       unzip $1     ;;
          *.Z)         uncompress $1;;
          *.7z)        7z x $1      ;;
          *.deb)       ar x $1      ;;
          *.tar.xz)    tar xf $1    ;;
          *.tar.zst)   unzstd $1    ;;
          *)           echo "'$1' cannot be extracted via ex()" ;;
        esac
    else
        echo "'$1' is not a valid file"
    fi
}

# Aliases

# Basic aliases
alias vim='nvim'
alias h='history'
alias df='df -h'
alias systemctl='sudo systemctl'
alias .='cd ..'
alias ..='cd ../../'
alias ...='cd ../../../'
alias .4='cd ../../../../'
alias .5='cd ../../../../../'

# Pacman aliases
alias syu='sudo pacman -Syu'
alias syyu='sudo pacman -Syyu'
alias remove='sudo pacman -Rns'
alias install='sudo pacman -S'

# Mirrorlist
alias mirror="sudo reflector -f 30 -l 30 --number 10 --verbose --save /etc/pacman.d/mirrorlist"
alias mirrord="sudo reflector --latest 50 --number 20 --sort delay --save /etc/pacman.d/mirrorlist"
alias mirrors="sudo reflector --latest 50 --number 20 --sort score --save /etc/pacman.d/mirrorlist"
alias mirrora="sudo reflector --latest 50 --number 20 --sort age --save /etc/pacman.d/mirrorlist"

# Listing 
alias ls='exa -al --color=always --group-directories-first'
alias lt='exa -aT --color=always --group-directories-first' # tree listing
alias l.='exa -a | grep -E "^\."'

# Grep coloring
alias grep='grep --color=auto'
alias egrep='grep -E --color=auto'
alias fgrep='grep -F --color=auto'

# Safety measures
alias cp='cp -i'
alias mv='mv -i'
alias rm='rm -i'

# GIT aliases
alias init='git init'
alias add='git add .'
alias commit='git commit -m'
alias stat='git status'
alias push='git push origin'
alias pull='git pull origin'
alias clone='git clone'

# Processes that eats memory & cpu
alias psmem='ps auxf | sort -nr -k 4 | head -10'
alias pscpu='ps auxf | sort -nr -k 3 | head -10'

# Verify signature for isos
alias gpg-check="gpg2 --keyserver-options auto-key-retrieve --verify"
# Receive the key of a developer
alias gpg-retrieve="gpg2 --keyserver-options auto-key-retrieve --receive-keys"

# Command prompt style
#PS1='[\u@\h \W]> '
#export PS1="\[\e[1;33m\][\u@\h \W]> \[\e[m\]"
PS1='\W\n> '
export PS1="\[\e[1;33m\]\W\n\[\e[1;33m\]> \[\e[m\]"

# SHOPT
shopt -s autocd # change to named directory
shopt -s cdspell # autocorrects cd misspellings
shopt -s cmdhist # save multi-line commands in history as single line
shopt -s dotglob
shopt -s histappend # do not overwrite history
shopt -s expand_aliases # expand aliases
shopt -s checkwinsize # checks term size when bash regains control


