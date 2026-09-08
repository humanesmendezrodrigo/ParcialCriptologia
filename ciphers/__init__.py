"""
Registro central de todos los cifrados del proyecto.

CIFRADOS es un diccionario donde cada entrada describe:
  - modulo: el módulo con las funciones cifrar(texto, clave) / descifrar(texto, clave)
  - requiere_clave: si el cifrado necesita que el usuario ingrese una clave
  - placeholder_clave: texto de ejemplo para el campo de clave en la GUI

La GUI (gui/app.py) arma el menú y las pantallas dinámicamente a partir
de este diccionario, sin necesidad de conocer el detalle de cada cifrado.

NOTA: descomenta los imports de los cifrados que ya estén implementados
por cada integrante. Los que falten pueden dejarse comentados sin que
el resto del programa se rompa.
"""

from . import pigpen
from . import cesar
from . import cesar_clave
from . import cesar_posicion
from . import vigenere
from . import polybios
from . import transposicion_grupos
from . import transposicion_series
from . import transposicion_columnas
from . import rail_fence
from . import adicion

CIFRADOS = {
    "Pigpen": {
        "modulo": pigpen,
        "requiere_clave": False,
        "placeholder_clave": "",
    },
    "César": {
        "modulo": cesar,
        "requiere_clave": True,
        "placeholder_clave": "Ej. 3",
    },
    "César con clave": {
        "modulo": cesar_clave,
        "requiere_clave": True,
        "placeholder_clave": "Ej. CLAVE",
    },
    "César con posición": {
        "modulo": cesar_posicion,
        "requiere_clave": True,
        "placeholder_clave": "Ej. 2",
    },
    "Vigenère": {
        "modulo": vigenere,
        "requiere_clave": True,
        "placeholder_clave": "Ej. CLAVE",
    },
    "Polybios": {
        "modulo": polybios,
        "requiere_clave": False,
        "placeholder_clave": "",
    },
    "Transposición por grupos": {
        "modulo": transposicion_grupos,
        "requiere_clave": True,
        "placeholder_clave": "Ej. 43521",
    },
    "Transposición por series": {
        "modulo": transposicion_series,
        "requiere_clave": False,
        "placeholder_clave": "",
    },
    "Transposición por columnas": {
        "modulo": transposicion_columnas,
        "requiere_clave": True,
        "placeholder_clave": "Ej. TRES",
    },
    "Rail fence": {
        "modulo": rail_fence,
        "requiere_clave": True,
        "placeholder_clave": "Ej. 3",
    },
    "Adición": {
        "modulo": adicion,
        "requiere_clave": True,
        "placeholder_clave": "Ej. 5",
    },
}
