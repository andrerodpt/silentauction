from subprocess import call
import os

def clear():
    _ = call('clear')
    ## For this to work you need to change the keybinding for "Terminal: Clear - workbench.action.terminal.clear" to "CTRL+K" in File -> Preferences -> Keyboard Shortcuts
