import os
import subprocess
from typing import List

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.extension.window_list import WindowList
from libqtile.layout.columns import Columns
from libqtile.layout.stack import Stack
from libqtile.layout.floating import Floating
from libqtile import hook, qtile
from subprocess import call

from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration

mod = "mod4"
browser = "brave"
terminal = "alacritty"
font = "JetBrainsMono Nerd Font Bold"

###### KEYBINDINGS ######
keys = [
    # Apps
    Key([mod], "b", lazy.spawn('brave'),
        desc="Launch Brave"),
    Key([mod], "Return", lazy.spawn(terminal),
        desc="Launch terminal"),
    Key([mod], "d", lazy.spawn('discord'),
        desc="Launch Discord"),
    Key([mod], "p", lazy.spawn('keepassxc'),
        desc="Launch Keepassxc"),
    Key([mod], "f", lazy.spawn('nemo'),
        desc="Launch File manager"),
    Key([mod], "v", lazy.spawn('virtualbox'),
        desc="Launch Virtualbox"),
    Key([mod], "o", lazy.spawn('obs'),
        desc="Launch OBS recorder"),
    Key([], "Print", lazy.spawn('flameshot'),
        desc="Launch Flameshot"),
    Key([mod], "s", lazy.spawn('slock'),
        desc="Launch Slock"),
    Key([mod, "shift"], "s", lazy.spawn('steam-runtime'),
        desc="Launch Slock"),


    # Toggle floating and fullscreen
    Key([mod, "shift"], "f", lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen mode"),
    Key([mod, "shift"], "space", lazy.window.toggle_floating(),
        desc="Toggle fullscreen mode"),

    # Switch between windows
    Key([mod], "h", lazy.layout.left(),
        desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(),
        desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(),
        desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(),
        desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(),
        desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(),
        desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(),
        desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    Key([mod, "shift"],"Return",lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(),
        desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(),
        desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(),
        desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(),
        desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    ]

##### GROUPS ######
groups = [
    Group('1', label="",
          matches=[Match(wm_class='brave-browser')],
          layout="columns"),
    Group('2', label="",
          matches=[Match(wm_class='alacritty')],
          layout="columns"),
    Group('3', label="",
          matches=[Match(wm_class='nemo')],
          layout="columns"),
    Group('4', label="󰙯",
          matches=[Match(wm_class='discord')],
          layout="columns"),
    Group('5', label="",
          matches=[Match(wm_class='virtualbox')],
          layout="columns"),
        ]
for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

###### LAYOUTS ######o

colors = [
    ["#002b36","#002b36"],
    ["#073642","#073642"],
    ["#586e75","#586e75"],
    ["#657b83","#657b83"],
    ["#839496","#839496"],
    ["#93a1a1","#93a1a1"],
    ["#eee8d5","#eee8d5"],
    ["#fdf6e3","#fdf6e3"],
    ["#ffff12","#ffff12"],
    ["#cb4b16","#cb4b16"],
    ["#d30102","#d30102"],
    ["#5b4e94","#5b4e94"],
    ["#268bd2","#268bd2"],
    ["#2aa198","#2aa198"],
    ["#5f8700","#5f8700"]]

layout_theme = {"border_width": 2,
                "margin": 4,
                "border_focus": colors[13],
                "border_normal": colors[1],
                }

layouts = [
    layout.Columns(**layout_theme),    
    layout.MonadTall(**layout_theme),
    layout.Floating(**layout_theme)
]

widget_defaults = dict(
    font=font,
    fontsize=13,
    padding=2,
    background=colors[13]
)

extension_defaults = widget_defaults.copy()

###### SCREEN AND WIDGETS ######
screens = [
    Screen(
        wallpaper='~/Pictures/Wallhaven/solarized-japan.png',
        wallpaper_mode='stretch',
        top=bar.Bar(
            [
                widget.GroupBox(
                       font = font,
                       fontsize = 15,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = colors[1],
                       inactive = colors[1],
                       rounded = False,
                       highlight_color = colors[13],
                       highlight_method = "line",
                       this_current_screen_border = colors[8],
                       this_screen_border = colors [8],
                       other_current_screen_border = colors[13],
                       other_screen_border = colors[13],
                       foreground = colors[1],
                       background = colors[13]
                ),
                widget.Spacer(
                       length=2,
                       background=colors[13]
                       ),
                widget.WindowName(
                       foreground = colors[6],
                       background = colors[1]
                       ),
                widget.Prompt(
                       foreground = colors[6],
                       background = colors[1]
                       ),
                widget.Systray(
                       foreground = colors[1],
                       background = colors[13]
                ),
                widget.Clock(
                    format=" %d-%m-%Y  %I:%M %p",
                    foreground = colors[9],
                    background = colors[13],
                    decorations=[
                           BorderDecoration(
                               colour = colors[13],
                               border_width = [0, 0, 2, 0],
                               padding_x = 5,
                               padding_y = None,
                           )
                       ],
                       ),
                #widget.Spacer(
                #        length=2,
                #        background=colors[1]
                #       ),
                widget.Net(
                       interface="enp3s0",
                       format = ' {down}↓↑{up}',
                       foreground = colors[10],
                       background = colors[13],
                       padding = 5,
                       decorations=[
                           BorderDecoration(
                               colour = colors[13],
                               border_width = [0, 0, 2, 0],
                               padding_x = 5,
                               padding_y = None,
                           )
                        ],
                        ),
                #widget.Spacer(
                #        length=2,
                #        background=colors[1]
                #        ),
                widget.CPU(
                    format = ' {freq_current}GHz {load_percent}%',
                    foreground = colors[11],
                    background = colors[13],
                    decorations=[
                           BorderDecoration(
                               colour = colors[13],
                               border_width = [0, 0, 2, 0],
                               padding_x = 5,
                               padding_y = None,
                           ),
                       ],
                       ),
                #widget.Spacer(
                #        length=2,
                #        background=colors[1]
                #       ),
                widget.Memory(
                       foreground = colors[8],
                       background = colors[13],
                       fmt = '{}',
                       measure_mem='G',
                       decorations=[
                           BorderDecoration(
                               colour =colors[13],
                               border_width = [0, 0, 2, 0],
                               padding_x = 5,
                               padding_y = None,
                           )
                       ],
                       ),
            ],
            20,
             #margin=[0, 8, 0, 8],  # Draw top and bottom borders
             border_color=["#2aa198", "#2aa198", "#2aa198", "#2aa198"],  
             opacity=0.8,
             background=colors[12],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
