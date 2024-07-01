<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/DanielPerezMoralesDev13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Tomar capturas de pantalla en Arch Linux***

**Para tomar capturas de pantalla en Arch Linux, puedes instalar `scrot` con el siguiente comando:**

```bash
sudo pacman -Syu scrot
```

---

## ***Información adicional***

- **Página oficial en Arch Linux:** *[scrot](https://archlinux.org/packages/extra/x86_64/scrot/ "https://archlinux.org/packages/extra/x86_64/scrot/")*
- **Repositorio GitHub:** *scrot es un proyecto de código abierto que puedes encontrar en [GitHub](https://github.com/resurrecting-open-source-projects/scrot "https://github.com/resurrecting-open-source-projects/scrot").*

- *Una vez instalado `scrot`, puedes configurar un atajo de teclado en Qtile para capturar pantalla. Para añadir un atajo de teclado en tu configuración de Qtile (`config.py`), puedes agregar una combinación de teclas similar a esta:*

```python
# Screenshot
Key([mod], "s", lazy.spawn("scrot")),
Key([mod, "shift"], "s", lazy.spawn("scrot -s")),
```

- *Esto te permitirá capturar fácilmente pantallas y personalizar la configuración según tus preferencias en Qtile en Arch Linux.*

**La configuracion completa seria:**

```python
# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielPerezMoralesDev13
# Correo electrónico: danielperezdev@proton.me 

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


from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from os import path
import subprocess

@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(path.expanduser(path = "~"), ".config", "qtile", 'autostart.sh')])

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    # Esta configuracion casi no se usa
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),


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
    
    # Esta configuracion casi no se usa
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

    # ? alacritty
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    
    
    # Esta configuracion casi no se usa
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # ------------ App Configs ------------

    # Menu
    Key([mod], "m", lazy.spawn("rofi -show drun")),

    # Window Nav
    Key([mod, "shift"], "m", lazy.spawn("rofi -show window")),

    # Browser
    Key([mod], "b", lazy.spawn("firefox")),

    # Screenshot
    Key([mod], "s", lazy.spawn("scrot")),
    Key([mod, "shift"], "s", lazy.spawn("scrot -s")),

    # ------------ Hardware Configs ------------

    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    Key([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-"))

]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


# Confirguracion por (Defecto)
# groups = [Group(i) for i in "123456789"]

# groups = [Group(i) for i in ["WWW", "DEV", "TERM", "MISC"]]

# Podes poner un maximo de 10 espacios de trabajo 0 - 9
groups = [Group(i) for i in ["󰖟", "", "", "󰆧"]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Cambiar a espacio de trabajo N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Enviar ventana al espacio de trabajo N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

# Confirguracion por (Defecto)
# for i in groups:
#     keys.extend(
#         [
#             # mod1 + group number = switch to group
#             Key(
#                 [mod],
#                 i.name,
#                 lazy.group[i.name].toscreen(),
#                 desc="Switch to group {}".format(i.name),
#             ),
#             # mod1 + shift + group number = switch to & move focused window to group
#             Key(
#                 [mod, "shift"],
#                 i.name,
#                 lazy.window.togroup(i.name, switch_group=True),
#                 desc="Switch to & move focused window to group {}".format(i.name),
#             ),
#             # Or, use below if you prefer not to switch to that group.
#             # # mod1 + shift + group number = move focused window to group
#             # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
#             #     desc="move focused window to group {}".format(i.name)),
#         ]
#     )

# Nueva Confirguracion
layout_conf = {
    'border_focus': '#F07178',
    'border_width': 1,
    'margin': 4
}

# Nueva Confirguracion
layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(**layout_conf),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(**layout_conf),
    layout.MonadWide(**layout_conf),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# Confirguracion por (Defecto)
# widget_defaults = dict(
#     font="sans",
#     fontsize=12,
#     padding=3,
# )

widget_defaults = dict(
    font="UbuntuMono Nerd Font Mono",
    fontsize=16,
    padding=3,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    foreground=["#f1ffff", "#f1ffff"],
                    background=["#0f101a", "#0f101a"],
                    font='UbuntuMono Nerd Font Mono',
                    fontsize=19,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active=["#f1ffff", "#f1ffff"],
                    inactive=["#f1ffff", "#f1ffff"],
                    rounded=False,
                    highlight_method='block',
                    urgent_alert_method='block', # <- linea agregada ... no he visto su uso
                    urgent_border=["#F07178", "#F07178"], # <- linea agregada ... no he visto su uso
                    this_current_screen_border=["#a151d3", "#a151d3"],
                    this_screen_border=["#353c4a", "#353c4a"],
                    other_current_screen_border=["#0f101a", "#0f101a"],
                    other_screen_border=["#0f101a", "#0f101a",],
                    disable_drag=True # <- linea agregada ... no he visto su uso
                ),
                # widget.GroupBox(),
                # widget.Prompt(),
                widget.WindowName(
                    foreground=["#a151d3", "#a151d3"],
                    background=["#0f101a", "#0f101a"],
                    fontsize=16,
                    font='UbuntuMono Nerd Font Mono',

                ),
                widget.Systray(),

                # Nueva Confirguracion
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    background=["#0f101a","#0f101a"]
                ),

                # Nueva Confirguracion
                widget.Image(
                    filename=path.join(path.expanduser("~"), ".config", "qtile", "img", "bar2.png")
                ),
                
                # Nueva Confirguracion
                widget.CurrentLayoutIcon(
                    scale=0.65,
                    foreground=["#0f101a","#0f101a"],
                    background=["#F07178","#F07178"] 
                ),

                # Confirguracion por (Defecto)
                # widget.CurrentLayout(),

                # Nueva Confirguracion
                widget.CurrentLayout(
                    foreground=["#0f101a","#0f101a"],
                    background=["#F07178","#F07178"],
                ),

                # Nueva Confirguracion
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    background=["#F07178","#F07178"]
                ),

                # Nueva Confirguracion
                widget.Image(
                    filename=path.join(path.expanduser("~"), ".config", "qtile", "img", "bar1.png")
                ),

                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # widget.TextBox("default config", name="default"),

                # Confirguracion por (Defecto)
                # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                
                # Nueva Confirguracion
                widget.TextBox(background=["#a151d3","#a151d3"], foreground=["#0f101a","#0f101a"],text=""), # nf-fa-clock_o

                # Confirguracion por (Defecto)
                # widget.Clock(format="%Y-%m-%d %a %I:%M %p"),

                # Nueva Confirguracion
                widget.Clock(background=["#a151d3","#a151d3"], foreground=["#0f101a","#0f101a"], padding=5, format='%d/%m/%Y - %H:%M:%S '),

                # widget.QuickExit(),
            ],
            26,
            opacity = 0.95
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
    # Configuración de la segunda pantalla (replicar según el número de pantallas)
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    foreground=["#f1ffff", "#f1ffff"],
                    background=["#0f101a", "#0f101a"],
                    font='UbuntuMono Nerd Font Mono',
                    fontsize=19,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active=["#f1ffff", "#f1ffff"],
                    inactive=["#f1ffff", "#f1ffff"],
                    rounded=False,
                    highlight_method='block',
                    urgent_alert_method='block', # <- linea agregada ... no he visto su uso
                    urgent_border=["#F07178", "#F07178"], # <- linea agregada ... no he visto su uso
                    this_current_screen_border=["#a151d3", "#a151d3"],
                    this_screen_border=["#353c4a", "#353c4a"],
                    other_current_screen_border=["#0f101a", "#0f101a"],
                    other_screen_border=["#0f101a", "#0f101a",],
                    disable_drag=True # <- linea agregada ... no he visto su uso
                ),
                # widget.GroupBox(),
                # widget.Prompt(),
                widget.WindowName(
                    foreground=["#a151d3", "#a151d3"],
                    background=["#0f101a", "#0f101a"],
                    fontsize=16,
                    font='UbuntuMono Nerd Font Mono',

                ),
                
                # Quitar el systray por que solo se vera en una pantalla
                # widget.Systray(),

                # Nueva Confirguracion
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    background=["#0f101a","#0f101a"]
                ),

                # Nueva Confirguracion
                widget.Image(
                    filename=path.join(path.expanduser("~"), ".config", "qtile", "img", "bar2.png")
                ),
                
                # Nueva Confirguracion
                widget.CurrentLayoutIcon(
                    scale=0.65,
                    foreground=["#0f101a","#0f101a"],
                    background=["#F07178","#F07178"] 
                ),

                # Confirguracion por (Defecto)
                # widget.CurrentLayout(),

                # Nueva Confirguracion
                widget.CurrentLayout(
                    foreground=["#0f101a","#0f101a"],
                    background=["#F07178","#F07178"],
                ),

                # Nueva Confirguracion
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    background=["#F07178","#F07178"]
                ),

                # Nueva Confirguracion
                widget.Image(
                    filename=path.join(path.expanduser("~"), ".config", "qtile", "img", "bar1.png")
                ),

                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # widget.TextBox("default config", name="default"),

                # Confirguracion por (Defecto)
                # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                
                # Nueva Confirguracion
                widget.TextBox(background=["#a151d3","#a151d3"], foreground=["#0f101a","#0f101a"],text=""), # nf-fa-clock_o

                # Confirguracion por (Defecto)
                # widget.Clock(format="%Y-%m-%d %a %I:%M %p"),

                # Nueva Confirguracion
                widget.Clock(background=["#a151d3","#a151d3"], foreground=["#0f101a","#0f101a"], padding=5, format='%d/%m/%Y - %H:%M:%S '),

                # widget.QuickExit(),
            ],
            26,
            opacity = 0.95
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# se Sobre escribido (por defecto)
# screens = [
#     Screen(
#         bottom=bar.Bar(
#             [
#                 widget.CurrentLayout(),
#                 widget.GroupBox(),
#                 widget.Prompt(),
#                 widget.WindowName(),
#                 widget.Chord(
#                     chords_colors={
#                         "launch": ("#ff0000", "#ffffff"),
#                     },
#                     name_transform=lambda name: name.upper(),
#                 ),
#                 widget.TextBox("default config", name="default"),
#                 widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
#                 # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
#                 # widget.StatusNotifier(),
#                 widget.Systray(),
#                 widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
#                 widget.QuickExit(),
#             ],
#             24,
#             # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
#             # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
#         ),
#         # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
#         # By default we handle these events delayed to already improve performance, however your system might still be struggling
#         # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
#         # x11_drag_polling_rate = 60,
#     ),
# ]

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
floats_kept_above = True
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
    ],
    # Nueva Confirguracion
    border_focus="#a151d3"
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
```
