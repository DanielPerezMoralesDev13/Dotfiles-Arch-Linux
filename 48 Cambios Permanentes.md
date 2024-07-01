<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/DanielPerezMoralesDev13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Cambios Permanentes***

*En sistemas Unix y similares, como Linux, los archivos `.xprofile` y `.xsession` son distintos y cumplen funciones diferentes en el entorno de escritorio X Window System (X11).*

- **`.xprofile`:** *Este archivo se utiliza para configurar el entorno del shell del usuario antes de que se inicie el entorno de escritorio. Aquí se pueden establecer variables de entorno, configuraciones del gestor de ventanas, lanzar aplicaciones, etc. Es específico para cada usuario y se ejecuta cada vez que un usuario inicia sesión en el sistema.*

- **`.xsession`:** *Este archivo, por otro lado, es utilizado para iniciar el entorno de escritorio completo de X11. Se ejecuta una vez cuando el usuario inicia sesión y generalmente se utiliza para iniciar el gestor de ventanas y cualquier otro servicio relacionado con el entorno de escritorio.*

*En resumen, `.xprofile` se utiliza para configuraciones específicas del shell del usuario, mientras que `.xsession` se utiliza para iniciar el entorno de escritorio completo.*

*Exactamente. El archivo `.xsession` se ejecuta una vez para cada sesión de usuario, independientemente de quién sea el usuario. Por lo tanto, se utiliza para configurar y lanzar el entorno de escritorio completo para todos los usuarios.*

*Por otro lado, el archivo `.xprofile` es específico para cada usuario. Se ejecuta cada vez que un usuario inicia sesión y se utiliza para configurar el entorno del shell del usuario antes de que se inicie el entorno de escritorio. Esto permite a cada usuario personalizar su propio entorno de trabajo de manera independiente.*

---

## ***Creación del Archivo `.xsession`***

**Primero, vamos a crear un archivo `.xsession` en el directorio de inicio (`$HOME`):**

```bash
touch ~/.xsession
```

- *Este archivo se utiliza para definir qué programas y configuraciones deben cargarse cuando se inicia una sesión de X.*

### ***Instalación de `xorg-xinit`***

- **Para asegurarnos de que `.xsession` funcione correctamente, necesitamos instalar `xorg-xinit`:**

```bash
sudo pacman -Syu xorg-xinit
```

- [*clonar un repositorio de Wallpapers*](https://github.com/DanielPerezMoralesDev13/Wallpapers.git "https://github.com/DanielPerezMoralesDev13/Wallpapers.git")

**Ahora, vamos a explicar el contenido del archivo `.xsession`:**

```bash
#!/bin/sh

userresources=$HOME/.Xresources
usermodmap=$HOME/.Xmodmap
sysresources=/etc/X11/xinit/.Xresources
sysmodmap=/etc/X11/xinit/.Xmodmap

# Merge in defaults and keymaps

if [ -f $sysresources ]; then
    xrdb -merge $sysresources
fi

if [ -f $sysmodmap ]; then
    xmodmap $sysmodmap
fi

if [ -f "$userresources" ]; then
    xrdb -merge "$userresources"
fi

if [ -f "$usermodmap" ]; then
    xmodmap "$usermodmap"
fi

# Start some nice programs

if [ -d /etc/X11/xinit/xinitrc.d ] ; then
    for f in /etc/X11/xinit/xinitrc.d/?*.sh ; do
        [ -x "$f" ] && . "$f"
    done
    unset f
fi

# Keyboard Layout
setxkbmap latam &

# Background image
feh --bg-scale /home/d4nitrix13/Wallpapers/Img/09.jpg

# Start PulseAudio
pulseaudio --start &
```
