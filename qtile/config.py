# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import subprocess

mod = "mod4"
alt = "mod1"
green = "#005500"
vgreen = "#20DF20"
black = "#181818"
gray = "#555555"
white = "#ffffff"
red = "#ff0000"
border_focus=vgreen;
border_width=2
margin=2
terminal = "alacritty" #guess_terminal()

def getVol():
   #return subprocess.check_output("wpctl get-volume @DEFAULT_AUDIO_SINK@ | cut -d \" \" -f 2 | sed \"s/\\.//\"", shell=True, text=True).strip() 
   return subprocess.check_output("wpctl get-volume @DEFAULT_AUDIO_SINK@ | sed \"s/[^0-9]*//g\"", shell=True, text=True).strip() 
def getLayout():
   return subprocess.check_output("xkb-switch -p", shell=True, text=True).strip() 
volUp = "wpctl set-volume @DEFAULT_AUDIO_SINK@ 0.05+"
volDown = "wpctl set-volume @DEFAULT_AUDIO_SINK@ 0.05-"
screenshot = "/home/user/scripts/maim.sh"
dmenuRun = "rofi -show run"
dmenuCustomRun = "/home/user/scripts/rofi_customrun.sh"
audio = "pavucontrol"
emotions = "/home/user/scripts/emo.sh"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod, "shift", "control"], "j", lazy.group.next_window(), desc="Move window focus to other window"),
    Key([mod, "shift", "control"], "k", lazy.group.prev_window(), desc="Move window focus to other window"),
    Key([mod], "space", lazy.group.prev_window(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "t", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "f", lazy.next_layout(), desc="Toggle between layouts"),
    #Key([mod], "f", lazy.hide_show_bar(), desc="Hides the bar"),

    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    #Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "r", lazy.spawn(dmenuCustomRun) ,desc="run "),
    Key([mod, "shift"], "r", lazy.spawn(dmenuRun), desc="Spawn a command using a prompt widget"),
    Key([], "Print", lazy.spawn(screenshot) ,desc="screenshot"),
    Key([mod], "b", lazy.hide_show_bar(), desc="Hides the bar"),
    Key([mod], "e", lazy.spawn(emotions) ,desc="emoji"),


    #Key([alt], "Shift_L",  lazy.widget["keyboardlayout"].next_keyboard() ),

    Key([mod], "v", lazy.spawn(volUp) ,desc="vol++"),
    Key([mod,"shift"], "v", lazy.spawn(volDown), desc="vol--"),
]

groups = [Group(i) for i in "1234567890"]

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
            # # mod1 + shift + letter of group = switch to & move focused window to group
            # Key(
            #     [mod, "shift"],
            #     i.name,
            #     lazy.window.togroup(i.name, switch_group=True),
            #     desc="Switch to & move focused window to group {}".format(i.name),
            # ),
            # # Or, use below if you prefer not to switch to that group.
            # mod1 + shift + letter of group = move focused window to group
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus=border_focus,border_normal=green, border_width=border_width, margin = margin),
    layout.Max(border_focus=border_focus, border_width=0),
    # Try more layouts by unleashing below layouts.
    #layout.Spiral(border_focus=border_focus, border_width=border_width),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(background=gray,highlight_method='block',active=vgreen,inactive=white,this_current_screen_border=green,this_screen_border=green,disable_drag=True),
                widget.CurrentLayoutIcon(background=green),
                widget.Sep(background=gray),
                widget.WindowName(),
                widget.Sep(background=gray),
                widget.Systray(),
                #widget.KeyboardLayout(configured_keyboards=['us','ru']),                
                widget.GenPollText(update_interval=0.2, func=lambda: getLayout(), mouse_callbacks={'Button1':lazy.spawn("xkb-switch -n")}),
                widget.GenPollText(update_interval=0.2, func=lambda: getVol()+"🔊", mouse_callbacks={'Button1':lazy.spawn(audio),'Button4':lazy.spawn(volUp),'Button5':lazy.spawn(volDown)}),
                widget.Clock(format="%T %a %d-%B (%m)-%Y",background=gray),
            ],
            24,
            border_width=[0, 0, border_width, 0],  # Draw top and bottom borders
            border_color=["000000", "000000", "005500", "000000"],  # Borders are magenta
            background=green,
            margin=[border_width-margin,0,-border_width,0],
        ),
        top=bar.Gap(-margin),
        left=bar.Gap(-margin),
        right=bar.Gap(-margin),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.toggle_floating()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        Match(wm_class="ripdrag"),  # ripdrag
        Match(wm_type='utility'),
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class='confirm'),
        Match(wm_class='dialog'),
        Match(wm_class='download'),
        Match(wm_class='error'),
        Match(wm_class='file_progress'),
        Match(wm_class='notification'),
        Match(wm_class='splash'),
        Match(wm_class='toolbar'),
        Match(title="floatterm"),  
        Match(wm_class='pavucontrol'),
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

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
