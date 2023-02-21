import os
import socket
import subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration


mod = "mod4"
browser = "google-chrome-stable"
terminal = "alacritty"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.

    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.

    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes

    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    # Kill window
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    # Restart Qtile
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),


    # My custom keybindings

    # Volume control
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "amixer -D pulse sset Master 5%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "amixer -D pulse sset Master 5%-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer -D pulse sset Master toggle")),

    # Brightness control
    Key([], "XF86MonBrightnessUp", lazy.spawn(
        "xbacklight -inc 10"), desc="Increase brightness",),
    Key([], "XF86MonBrightnessDown", lazy.spawn(
        "xbacklight -dec 10"), desc="Decrease brightness",),

    # Screenshot
    Key([], "Print", lazy.spawn("flameshot gui"), desc="Take a screenshot",),

    # Terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Browser
    Key([mod], "b", lazy.spawn("google-chrome-stable"), desc="Launch browser"),

    # File manager
    Key([mod], "t", lazy.spawn("thunar"), desc="Launch file manager"),

    # Vscode
    Key([mod], "v", lazy.spawn("code"), desc="Launch vscode"),

    # Emacs

    Key([mod], "e", lazy.spawn("emacsclient -c -a emacs"), desc="Launch emacs"),

    # Obsidian

    Key([mod], "o", lazy.spawn("obsidian"), desc="Launch obsidian"),

    # dmenu

    Key([mod], "p", lazy.spawn("dmenu_run"), desc="Launch dmenu"),

]

groups = [Group(i) for i in "12345"]

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
                desc="Switch to & move focused window to group {}".format(
                    i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layout_theme = {"border_width": 2,
                "margin": 8,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }

layouts = [
    layout.MonadTall(**layout_theme),
]

colors = [["#282c34", "#282c34"],
          ["#1c1f24", "#1c1f24"],
          ["#dfdfdf", "#dfdfdf"],
          ["#ff6c6b", "#ff6c6b"],
          ["#98be65", "#98be65"],
          ["#da8548", "#da8548"],
          ["#51afef", "#51afef"],
          ["#c678dd", "#c678dd"],
          ["#46d9ff", "#46d9ff"],
          ["#a9a1e1", "#a9a1e1"]]

widget_defaults = dict(
    font="Fira Code",
    fontsize=12,
    padding=2,
    background=colors[0]
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper="/home/johnny/Pictures/wallpapers/wp8112582.jpg",
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.Sep(
                       linewidth=0,
                       padding=6,
                       foreground=colors[2],
                       background=colors[0]
                ),
                widget.Image(
                    filename="~/.config/qtile/icons/python-white.png",
                    scale="False"
                ),
                widget.Sep(
                    linewidth=0,
                    padding=6,
                    foreground=colors[2],
                    background=colors[0]
                ),
                widget.GroupBox(
                    font="Ubuntu Bold",
                    fontsize=9,
                    margin_y=3,
                    margin_x=0,
                    padding_y=5,
                    padding_x=3,
                    borderwidth=3,
                    active=colors[2],
                    inactive=colors[7],
                    rounded=False,
                    highlight_color=colors[1],
                    highlight_method="line",
                    this_current_screen_border=colors[6],
                    this_screen_border=colors[4],
                    other_current_screen_border=colors[6],
                    other_screen_border=colors[4],
                    foreground=colors[2],
                    background=colors[0]
                ),
                widget.TextBox(
                    text='|',
                    font="Ubuntu Mono",
                    background=colors[0],
                    foreground='474747',
                    padding=2,
                    fontsize=14
                ),
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                    foreground=colors[2],
                    background=colors[0],
                    padding=0,
                    scale=0.7
                ),
                widget.CurrentLayout(
                    foreground=colors[2],
                    background=colors[0],
                    padding=5
                ),
                widget.TextBox(
                    text='|',
                    font="Ubuntu Mono",
                    background=colors[0],
                    foreground='474747',
                    padding=2,
                    fontsize=14
                ),
                widget.WindowName(
                    foreground=colors[6],
                    background=colors[0],
                    padding=0
                ),
                widget.Sep(
                    linewidth=0,
                    padding=6,
                    foreground=colors[0],
                    background=colors[0]
                ),
                widget.Net(
                    interface="enp6s0",
                    format='Net: {down} ↓↑ {up}',
                    foreground=colors[3],
                    background=colors[0],
                    padding=5,
                    decorations=[
                        BorderDecoration(
                            colour=colors[3],
                            border_width=[0, 0, 2, 0],
                            padding_x=5,
                            padding_y=None,
                        )
                    ],
                ),
                widget.Sep(
                    linewidth=0,
                    padding=6,
                    foreground=colors[0],
                    background=colors[0]
                ),        
                widget.Memory(
                    foreground=colors[9],
                    background=colors[0],
                    fmt='Mem: {}',
                    padding=5,
                    decorations=[
                        BorderDecoration(
                            colour=colors[9],
                            border_width=[0, 0, 2, 0],
                            padding_x=5,
                            padding_y=None,
                        )
                    ],
                ),
                widget.Sep(
                    linewidth=0,
                    padding=6,
                    foreground=colors[0],
                    background=colors[0]
                ),
                widget.Volume(
                    foreground=colors[7],
                    background=colors[0],
                    fmt='Vol: {}',
                    padding=5,
                    decorations=[
                        BorderDecoration(
                            colour=colors[7],
                            border_width=[0, 0, 2, 0],
                            padding_x=5,
                            padding_y=None,
                        )
                    ],
                ),
                widget.Sep(
                    linewidth=0,
                    padding=6,
                    foreground=colors[0],
                    background=colors[0]
                ),

                widget.KeyboardLayout(
                    foreground=colors[8],
                    background=colors[0],
                    fmt='Keyboard: {}',
                    padding=5,
                    decorations=[
                        BorderDecoration(
                            colour=colors[8],
                            border_width=[0, 0, 2, 0],
                            padding_x=5,
                            padding_y=None,
                        )
                    ],
                ),
                widget.Sep(
                    linewidth=0,
                    padding=6,
                    foreground=colors[0],
                    background=colors[0]
                ),

                widget.Clock(
                    foreground=colors[6],
                    background=colors[0],
                    format="%A, %B %d - %H:%M ",
                    decorations=[
                        BorderDecoration(
                            colour=colors[6],
                            border_width=[0, 0, 2, 0],
                            padding_x=5,
                            padding_y=None,
                        )
                    ],

                ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                )

            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),

    ),

]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
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
auto_minimize = True
wl_input_rules = None

# Auto start applications


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])


wmname = "LG3D"
