# Generador de VLANs

Este script en Python crea configuraciones de VLAN utilizando una interfaz gráfica de usuario (GUI) construida con Tkinter.

## Descripción

Este script genera configuraciones de VLAN basadas en la entrada del usuario a través de una interfaz gráfica. Permite a los usuarios especificar el número de VLANs que se generarán y sus nombres correspondientes. Las configuraciones de VLAN generadas pueden guardarse en un archivo o copiarse en el portapapeles.

## Requisitos

- Python 3.x
- Biblioteca Tkinter

## Uso

1. Descargue el archivo
2. Ejecute el archivo

## Funcionalidad
.
- **generate_vlans():** Genera comandos de VLAN basados en los nombres de VLAN proporcionados por el usuario.
- **save_vlans():** Guarda los comandos de VLAN generados en un archivo llamado "vlans.txt".
- **copy_vlans():** Copia los comandos de VLAN generados al portapapeles.
- **clear_vlans():** Borra los campos de entrada y restablece la interfaz.


## Componentes de la GUI

- Campo de entrada para especificar el número de VLANs.
- Botones para proceder, generar VLANs, guardar comandos, copiar VLANs y borrar campos.
- Área de texto para mostrar los comandos de VLAN generados.
- Barra de desplazamiento para desplazarse por los nombres de VLAN.

## Autor

Este script fue creado por Zaphkie1.

## Licencia

Este proyecto está licenciado bajo la Licencia GNU General Public License v3.0
