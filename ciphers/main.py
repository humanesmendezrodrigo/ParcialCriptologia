# ==========================================
# INTERFAZ GRAFICA - CIFRADO CESAR
# ==========================================

import tkinter as tk
from tkinter import ttk, messagebox

from cesar_clave import cifrar as cifrar_clave
from cesar_clave import descifrar as descifrar_clave

from cesar_posicion import cifrar as cifrar_posicion
from cesar_posicion import descifrar as descifrar_posicion


# ==========================================
# FUNCIONES DE LA INTERFAZ
# ==========================================

def obtener_valor():
    """
    Obtiene la clave o posición ingresada.
    """
    try:
        return int(entrada_valor.get())
    except ValueError:
        messagebox.showerror(
            "Error",
            "Debe ingresar un número válido."
        )
        return None


def cifrar_mensaje():
    """
    Cifra el mensaje utilizando
    el método seleccionado.
    """

    mensaje = entrada_mensaje.get("1.0", tk.END).strip()

    if not mensaje:
        messagebox.showwarning(
            "Advertencia",
            "Ingrese un mensaje para cifrar."
        )
        return

    valor = obtener_valor()

    if valor is None:
        return

    metodo = combo_metodo.get()

    if metodo == "César con clave":

        resultado = cifrar_clave(
            mensaje,
            valor
        )

    elif metodo == "César con posición":

        resultado = cifrar_posicion(
            mensaje,
            valor
        )

    else:

        messagebox.showerror(
            "Error",
            "Seleccione un método."
        )
        return

    mostrar_resultado(resultado)


def descifrar_mensaje():
    """
    Descifra el mensaje utilizando
    el método seleccionado.
    """

    mensaje = entrada_mensaje.get("1.0", tk.END).strip()

    if not mensaje:
        messagebox.showwarning(
            "Advertencia",
            "Ingrese un mensaje para descifrar."
        )
        return

    valor = obtener_valor()

    if valor is None:
        return

    metodo = combo_metodo.get()

    if metodo == "César con clave":

        resultado = descifrar_clave(
            mensaje,
            valor
        )

    elif metodo == "César con posición":

        resultado = descifrar_posicion(
            mensaje,
            valor
        )

    else:

        messagebox.showerror(
            "Error",
            "Seleccione un método."
        )
        return

    mostrar_resultado(resultado)


def mostrar_resultado(resultado):
    """
    Muestra el resultado en la caja de texto.
    """

    salida_resultado.config(state="normal")

    salida_resultado.delete(
        "1.0",
        tk.END
    )

    salida_resultado.insert(
        tk.END,
        resultado
    )

    salida_resultado.config(state="disabled")


def copiar_resultado():
    """
    Copia el resultado al portapapeles.
    """

    resultado = salida_resultado.get(
        "1.0",
        tk.END
    ).strip()

    if not resultado:
        messagebox.showwarning(
            "Advertencia",
            "No existe ningún resultado para copiar."
        )
        return

    ventana.clipboard_clear()
    ventana.clipboard_append(resultado)

    messagebox.showinfo(
        "Copiado",
        "El resultado fue copiado correctamente."
    )


def limpiar():
    """
    Limpia todos los campos.
    """

    entrada_mensaje.delete(
        "1.0",
        tk.END
    )

    entrada_valor.delete(
        0,
        tk.END
    )

    entrada_valor.insert(
        0,
        "3"
    )

    salida_resultado.config(
        state="normal"
    )

    salida_resultado.delete(
        "1.0",
        tk.END
    )

    salida_resultado.config(
        state="disabled"
    )


# ==========================================
# CREAR VENTANA
# ==========================================

ventana = tk.Tk()

ventana.title(
    "Sistema de Cifrado César"
)

ventana.geometry(
    "700x650"
)

ventana.resizable(
    False,
    False
)


# ==========================================
# TITULO
# ==========================================

titulo = tk.Label(
    ventana,
    text="🔐 SISTEMA DE CIFRADO CÉSAR",
    font=("Arial", 22, "bold")
)

titulo.pack(
    pady=20
)


subtitulo = tk.Label(
    ventana,
    text="Cifrado y descifrado mediante clave o posición",
    font=("Arial", 11)
)

subtitulo.pack(
    pady=5
)


# ==========================================
# FRAME PRINCIPAL
# ==========================================

frame = tk.Frame(
    ventana
)

frame.pack(
    padx=40,
    pady=15,
    fill="both"
)


# ==========================================
# MENSAJE
# ==========================================

label_mensaje = tk.Label(
    frame,
    text="Mensaje:",
    font=("Arial", 12, "bold")
)

label_mensaje.pack(
    anchor="w"
)


entrada_mensaje = tk.Text(
    frame,
    height=6,
    width=70,
    font=("Arial", 12)
)

entrada_mensaje.pack(
    pady=8
)


# ==========================================
# METODO
# ==========================================

label_metodo = tk.Label(
    frame,
    text="Método de cifrado:",
    font=("Arial", 12, "bold")
)

label_metodo.pack(
    anchor="w",
    pady=(10, 5)
)


combo_metodo = ttk.Combobox(
    frame,
    values=[
        "César con clave",
        "César con posición"
    ],
    state="readonly",
    width=30,
    font=("Arial", 11)
)

combo_metodo.pack(
    anchor="w"
)

combo_metodo.current(0)


# ==========================================
# CLAVE / POSICION
# ==========================================

label_valor = tk.Label(
    frame,
    text="Clave / Posición:",
    font=("Arial", 12, "bold")
)

label_valor.pack(
    anchor="w",
    pady=(15, 5)
)


entrada_valor = tk.Entry(
    frame,
    width=15,
    font=("Arial", 12)
)

entrada_valor.pack(
    anchor="w"
)

entrada_valor.insert(
    0,
    "3"
)


# ==========================================
# BOTONES
# ==========================================

frame_botones = tk.Frame(
    frame
)

frame_botones.pack(
    pady=20
)


boton_cifrar = tk.Button(
    frame_botones,
    text="🔒 CIFRAR",
    command=cifrar_mensaje,
    font=("Arial", 11, "bold"),
    width=15,
    height=2
)

boton_cifrar.grid(
    row=0,
    column=0,
    padx=10
)


boton_descifrar = tk.Button(
    frame_botones,
    text="🔓 DESCIFRAR",
    command=descifrar_mensaje,
    font=("Arial", 11, "bold"),
    width=15,
    height=2
)

boton_descifrar.grid(
    row=0,
    column=1,
    padx=10
)


# ==========================================
# RESULTADO
# ==========================================

label_resultado = tk.Label(
    frame,
    text="Resultado:",
    font=("Arial", 12, "bold")
)

label_resultado.pack(
    anchor="w"
)


salida_resultado = tk.Text(
    frame,
    height=6,
    width=70,
    font=("Arial", 12)
)

salida_resultado.pack(
    pady=8
)

salida_resultado.config(
    state="disabled"
)


# ==========================================
# BOTONES INFERIORES
# ==========================================

frame_inferior = tk.Frame(
    frame
)

frame_inferior.pack(
    pady=15
)


boton_copiar = tk.Button(
    frame_inferior,
    text="📋 COPIAR",
    command=copiar_resultado,
    font=("Arial", 10, "bold"),
    width=15
)

boton_copiar.grid(
    row=0,
    column=0,
    padx=10
)


boton_limpiar = tk.Button(
    frame_inferior,
    text="🗑 LIMPIAR",
    command=limpiar,
    font=("Arial", 10, "bold"),
    width=15
)

boton_limpiar.grid(
    row=0,
    column=1,
    padx=10
)


# ==========================================
# PIE DE VENTANA
# ==========================================

pie = tk.Label(
    ventana,
    text="Proyecto de Criptografía - Cifrado César",
    font=("Arial", 9)
)

pie.pack(
    pady=10
)


# ==========================================
# EJECUTAR APLICACION
# ==========================================

ventana.mainloop()