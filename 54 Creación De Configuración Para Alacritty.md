<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/DanielPerezMoralesDev13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Creación de Configuración para Alacritty***

**Vamos a crear un directorio y un archivo de configuración para Alacritty:**

```bash
mkdir -p ~/.config/alacritty
touch ~/.config/alacritty/alacritty.toml
```

**Luego, agregamos las siguientes líneas al archivo `alacritty.toml`:**

- *[**Ejemplos de como configurar alacritty.toml**](https://convoluted.bearblog.dev/alacritty-config-example-guide/ "https://convoluted.bearblog.dev/alacritty-config-example-guide/")*

- *[**Ejemplos de como configurar alacritty.toml**](https://gist.github.com/ritog/76081f97681e7079d11ec163a5bd4141 "https://gist.github.com/ritog/76081f97681e7079d11ec163a5bd4141")*

```toml
# $HOME/.config/alacritty/alacritty.toml
# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielPerezMoralesDev13
# Correo electrónico: danielperezdev@proton.me 

[window]
opacity = 0.9
```

- **`mkdir -p ~/.config/alacritty`:** *Crea el directorio `.config/alacritty` si no existe.*
- **`touch ~/.config/alacritty/alacritty.toml`:** *Crea el archivo de configuración `alacritty.toml` dentro del directorio `.config/alacritty`.*
- **`opacity = 0.9`:** *Establece la opacidad de las ventanas de Alacritty en un 90%. Esta configuración se encuentra dentro de la sección `[window]` del archivo de configuración.*

- *Con estas configuraciones, habrás instalado `picom`, configurado su ejecución en el inicio de sesión, y creado una configuración inicial para Alacritty que establece la opacidad de las ventanas.*
