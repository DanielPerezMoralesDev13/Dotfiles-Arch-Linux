<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/DanielPerezMoralesDev13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# jaja

eres experto en arch linux me diras como funciona este paquete a bajo nivel
pagina de instalacion de arch linux del paquete
repositorio de github del paquete
pagina oficial del paquete si tiene si no pon no disponible

sudo pacman -S code -> no recomendada

alt + z alternanar linea

---

min 0:0

vlc /mnt/windows-d/Escritorio/Daniel\ Perez\ Morales/mastermind\ cursos/#2informatica/#2Introducción\ a\ Linux/#2Linux\ Creando\ tu\ propio\ entorno\ de\ escritorio\ en\ Arch/#1Gestores\ de\ ventanas/#11

<!-- ## importante commit 393fa8f -->

<!-- ## importante commit b4b16fa -->

## importante commit 83fb32e

fichero -> 30

---

atajo de teclado vscode y firefox ctrl + w cierra ventana

---

<!-- todo -->

instalar psutils y python-pip python-psutil

```bash
pacman -Ss psutil
extra/psutils 3.3.2-2
    A set of postscript utilities
extra/python-psutil 5.9.8-4
    A cross-platform process and system utilities module for Python
extra/texlive-fontutils 2024.2-2 (texlive)
    TeX Live - Graphics and font utilities
```

```bash
sudo pacman -S python-psutil
```

instalar checkupdates

sudo pacman -Syu pacman-contrib

ventana floante

mod shift f

instalamos para mas transparencia

sudo pacman -Syu --noconfirm redshift

crear un directorio themes

cp -r ~/dotfiles/.theme/ ~/

cp -r ~/dotfiles/.config/alacritty/ ~/

tema lightdm

sudo pacman -Syu --noconfirm lightdm-webkit2-greeter

Remplazar

nano /etc/lightdm/lightdm.conf

```bash
# greeter-session=example-gtk-gnome
greeter-session=lightdm-webkit2-greeter
```

---

**Restructuracion del Directorio de configuracion de qtile `~/.config/qtile/`:**

```bash
tree -C 
.
├── autostart.sh
├── config.json
├── config.py
├── README.md
├── settings
│   ├── groups.py
│   ├── keys.py
│   ├── layouts.py
│   ├── mouse.py
│   ├── path.py
│   ├── screens.py
│   ├── theme.py
│   └── widgets.py
└── themes
    ├── dark-grey
    │   ├── colors.json
    │   └── img
    │       ├── bar1.png
    │       ├── bar2.png
    │       ├── bar3.png
    │       └── bar4.png
    ├── dracula
    │   ├── colors.json
    │   └── img
    │       ├── bar1.png
    │       ├── bar2.png
    │       ├── bar3.png
    │       └── bar4.png
    ├── material-ocean
    │   ├── colors.json
    │   └── img
    │       ├── bar1.png
    │       ├── bar2.png
    │       ├── bar3.png
    │       └── bar4.png
    ├── onedark
    │   ├── colors.json
    │   └── img
    │       ├── bar1.png
    │       ├── bar2.png
    │       ├── bar3.png
    │       └── bar4.png
    └── README.md

11 directories, 33 files
```

---

gestor de archivos de terminal

---
