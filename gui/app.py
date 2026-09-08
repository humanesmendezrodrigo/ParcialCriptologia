"""
Interfaz gráfica principal del proyecto.

Muestra en un panel izquierdo la lista de todos los cifrados
(tomada de ciphers.CIFRADOS) y, al hacer clic en uno, arma en el
panel derecho un formulario con:
  - campo de mensaje
  - campo de clave (solo si el cifrado lo requiere)
  - botones Cifrar / Descifrar
  - área de resultado

No conoce el detalle interno de ningún cifrado: solo llama a
funcion(texto, clave) o funcion(texto) según corresponda.
"""

import tkinter as tk
from tkinter import ttk, messagebox

from ciphers import CIFRADOS


class CifradorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cifrador - Proyecto de Criptografía")
        self.geometry("800x520")
        self.resizable(False, False)

        self.cifrado_actual = None
        self.entrada_clave = None
        self.texto_entrada = None
        self.texto_resultado = None

        self._construir_layout()

    def _construir_layout(self):
        panel_izquierdo = ttk.Frame(self, padding=10)
        panel_izquierdo.pack(side="left", fill="y")

        ttk.Label(
            panel_izquierdo, text="Tipos de cifrado", font=("Arial", 12, "bold")
        ).pack(pady=(0, 10))

        for nombre in CIFRADOS:
            ttk.Button(
                panel_izquierdo,
                text=nombre,
                width=26,
                command=lambda n=nombre: self._mostrar_cifrado(n),
            ).pack(pady=2)

        self.panel_derecho = ttk.Frame(self, padding=15)
        self.panel_derecho.pack(side="right", fill="both", expand=True)

        ttk.Label(
            self.panel_derecho,
            text="Selecciona un cifrado de la izquierda",
            font=("Arial", 14, "bold"),
        ).pack(anchor="w")

    def _mostrar_cifrado(self, nombre):
        self.cifrado_actual = nombre
        info = CIFRADOS[nombre]

        for widget in self.panel_derecho.winfo_children():
            widget.destroy()

        ttk.Label(self.panel_derecho, text=nombre, font=("Arial", 14, "bold")).pack(
            anchor="w", pady=(0, 10)
        )

        ttk.Label(self.panel_derecho, text="Mensaje:").pack(anchor="w")
        self.texto_entrada = tk.Text(self.panel_derecho, height=5, width=70)
        self.texto_entrada.pack(pady=(0, 10))

        self.entrada_clave = None
        if info["requiere_clave"]:
            ttk.Label(self.panel_derecho, text="Clave:").pack(anchor="w")
            self.entrada_clave = ttk.Entry(self.panel_derecho, width=30)
            self.entrada_clave.pack(pady=(0, 10))

        frame_botones = ttk.Frame(self.panel_derecho)
        frame_botones.pack(pady=(0, 10))
        ttk.Button(frame_botones, text="Cifrar", command=self._cifrar).pack(
            side="left", padx=5
        )
        ttk.Button(frame_botones, text="Descifrar", command=self._descifrar).pack(
            side="left", padx=5
        )

        ttk.Label(self.panel_derecho, text="Resultado:").pack(anchor="w")
        self.texto_resultado = tk.Text(
            self.panel_derecho, height=5, width=70, state="disabled"
        )
        self.texto_resultado.pack()

    def _cifrar(self):
        self._ejecutar("cifrar")

    def _descifrar(self):
        self._ejecutar("descifrar")

    def _ejecutar(self, operacion):
        info = CIFRADOS[self.cifrado_actual]
        texto = self.texto_entrada.get("1.0", "end").strip()

        if not texto:
            messagebox.showwarning("Falta mensaje", "Escribe un mensaje primero.")
            return

        clave = None
        if info["requiere_clave"]:
            clave = self.entrada_clave.get().strip()
            if not clave:
                messagebox.showwarning("Falta clave", "Este cifrado necesita una clave.")
                return

        funcion = getattr(info["modulo"], operacion)
        try:
            resultado = funcion(texto, clave) if info["requiere_clave"] else funcion(texto)
        except Exception as error:
            messagebox.showerror("Error", f"No se pudo procesar: {error}")
            return

        self.texto_resultado.config(state="normal")
        self.texto_resultado.delete("1.0", "end")
        self.texto_resultado.insert("1.0", resultado)
        self.texto_resultado.config(state="disabled")


def iniciar_app():
    app = CifradorApp()
    app.mainloop()
