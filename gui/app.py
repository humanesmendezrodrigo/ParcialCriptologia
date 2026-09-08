"""Interfaz gráfica para los cifrados registrados en :mod:`ciphers`."""

import re
import tkinter as tk
from tkinter import messagebox, ttk

from ciphers import CIFRADOS


DETALLES = {
    "Pigpen": "Representa las letras con símbolos. Para descifrar, mantén un espacio entre cada símbolo.",
    "César": "Desplaza cada letra la cantidad indicada. La clave debe ser un número entero.",
    "César con clave": "Este módulo usa una clave numérica como desplazamiento entero.",
    "César con posición": "Desplaza cada letra desde la posición indicada. Usa un número entero.",
    "Vigenère": "Usa una palabra formada solo por letras como clave.",
    "Polybios": "Convierte letras en coordenadas; I y J comparten posición. Los signos de puntuación no se conservan.",
    "Transposición por grupos": "La clave debe contener una vez cada número del 1 al tamaño de la clave, por ejemplo 43521.",
    "Transposición por series": "Reordena las posiciones y elimina los espacios del mensaje.",
    "Transposición por columnas": "Ordena según la clave; elimina espacios y agrega X al final para completar columnas.",
    "Rail fence": "Escribe el número entero de rieles que se utilizarán.",
    "Adición": "Cifra como una secuencia de números. Para descifrar, escribe números separados por espacios o comas.",
}

CLAVES_ENTERAS = {"César", "César con clave", "César con posición", "Rail fence"}
EJEMPLOS_NUMERICOS = {nombre: "Ej. 3" for nombre in CLAVES_ENTERAS}


class CifradorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CriptoLab · Cifrados clásicos")
        self.geometry("1080x700")
        self.minsize(900, 580)
        self.configure(bg="#f4f7fb")
        self.cifrado_actual = None
        self.ejemplo_clave = ""
        self.entrada_clave = self.texto_entrada = self.texto_resultado = None
        self._configurar_estilos()
        self._construir_layout()

    def _configurar_estilos(self):
        estilo = ttk.Style(self)
        estilo.theme_use("clam")
        estilo.configure("App.TFrame", background="#f4f7fb")
        estilo.configure("Sidebar.TFrame", background="#102a43")
        estilo.configure("Card.TFrame", background="#ffffff")
        estilo.configure("Title.TLabel", background="#102a43", foreground="#ffffff", font=("Segoe UI", 20, "bold"))
        estilo.configure("Subtitle.TLabel", background="#102a43", foreground="#cbd8e6", font=("Segoe UI", 10))
        estilo.configure("MenuTitle.TLabel", background="#102a43", foreground="#eaf2f8", font=("Segoe UI", 11, "bold"))
        estilo.configure("Heading.TLabel", background="#ffffff", foreground="#102a43", font=("Segoe UI", 18, "bold"))
        estilo.configure("Body.TLabel", background="#ffffff", foreground="#334e68", font=("Segoe UI", 10))
        estilo.configure("Field.TLabel", background="#ffffff", foreground="#243b53", font=("Segoe UI", 10, "bold"))
        estilo.configure("Cipher.TButton", background="#1f4d78", foreground="#ffffff", font=("Segoe UI", 10), padding=(12, 8), borderwidth=0)
        estilo.map("Cipher.TButton", background=[("active", "#3476aa")])
        estilo.configure("Primary.TButton", background="#117a65", foreground="#ffffff", font=("Segoe UI", 10, "bold"), padding=(18, 9), borderwidth=0)
        estilo.map("Primary.TButton", background=[("active", "#0b5d4c")])
        estilo.configure("Secondary.TButton", background="#e7eef6", foreground="#243b53", font=("Segoe UI", 10, "bold"), padding=(14, 9), borderwidth=0)
        estilo.map("Secondary.TButton", background=[("active", "#d5e2ef")])
        estilo.configure("TEntry", padding=8)

    def _construir_layout(self):
        contenedor = ttk.Frame(self, style="App.TFrame", padding=18)
        contenedor.pack(fill="both", expand=True)
        contenedor.columnconfigure(1, weight=1)
        contenedor.rowconfigure(0, weight=1)
        lateral = ttk.Frame(contenedor, style="Sidebar.TFrame", padding=18)
        lateral.grid(row=0, column=0, sticky="nsw", padx=(0, 18))
        ttk.Label(lateral, text="CriptoLab", style="Title.TLabel").pack(anchor="w")
        ttk.Label(lateral, text="Cifrados clásicos", style="Subtitle.TLabel").pack(anchor="w", pady=(0, 28))
        ttk.Label(lateral, text="ELIGE UN MÉTODO", style="MenuTitle.TLabel").pack(anchor="w", pady=(0, 8))
        for nombre in CIFRADOS:
            ttk.Button(lateral, text=nombre, style="Cipher.TButton", width=28, command=lambda n=nombre: self._mostrar_cifrado(n)).pack(fill="x", pady=3)
        self.panel_derecho = ttk.Frame(contenedor, style="Card.TFrame", padding=28)
        self.panel_derecho.grid(row=0, column=1, sticky="nsew")
        self._mostrar_bienvenida()

    def _mostrar_bienvenida(self):
        ttk.Label(self.panel_derecho, text="Explora los cifrados", style="Heading.TLabel").pack(anchor="w", pady=(55, 8))
        ttk.Label(self.panel_derecho, text="Selecciona un método en el panel lateral para cifrar o descifrar un mensaje.", style="Body.TLabel", wraplength=610).pack(anchor="w")

    def _mostrar_cifrado(self, nombre):
        self.cifrado_actual = nombre
        info = CIFRADOS[nombre]
        for widget in self.panel_derecho.winfo_children():
            widget.destroy()
        ttk.Label(self.panel_derecho, text=nombre, style="Heading.TLabel").pack(anchor="w")
        ttk.Label(self.panel_derecho, text=DETALLES[nombre], style="Body.TLabel", wraplength=650, justify="left").pack(anchor="w", pady=(5, 20))
        ttk.Label(self.panel_derecho, text="Mensaje", style="Field.TLabel").pack(anchor="w")
        self.texto_entrada = tk.Text(self.panel_derecho, height=7, wrap="word", font=("Segoe UI", 11), bg="#f8fbff", fg="#243b53", insertbackground="#102a43", relief="flat", highlightthickness=1, highlightbackground="#cbd8e6", highlightcolor="#3476aa", padx=10, pady=8)
        self.texto_entrada.pack(fill="x", pady=(6, 16))
        self.entrada_clave = None
        if info["requiere_clave"]:
            etiqueta = "Clave numérica" if nombre in CLAVES_ENTERAS else "Clave"
            ttk.Label(self.panel_derecho, text=etiqueta, style="Field.TLabel").pack(anchor="w")
            self.entrada_clave = ttk.Entry(self.panel_derecho, width=38)
            self.ejemplo_clave = EJEMPLOS_NUMERICOS.get(nombre, info["placeholder_clave"])
            self.entrada_clave.insert(0, self.ejemplo_clave)
            self.entrada_clave.pack(anchor="w", pady=(6, 18))
            self.entrada_clave.bind("<FocusIn>", self._limpiar_ejemplo_clave)
        botones = ttk.Frame(self.panel_derecho, style="Card.TFrame")
        botones.pack(anchor="w", pady=(0, 20))
        ttk.Button(botones, text="Cifrar", style="Primary.TButton", command=self._cifrar).pack(side="left", padx=(0, 8))
        ttk.Button(botones, text="Descifrar", style="Secondary.TButton", command=self._descifrar).pack(side="left", padx=(0, 8))
        ttk.Button(botones, text="Limpiar", style="Secondary.TButton", command=self._limpiar_campos).pack(side="left")
        resultado_fila = ttk.Frame(self.panel_derecho, style="Card.TFrame")
        resultado_fila.pack(fill="x")
        ttk.Label(resultado_fila, text="Resultado", style="Field.TLabel").pack(side="left")
        ttk.Button(resultado_fila, text="Copiar", style="Secondary.TButton", command=self._copiar_resultado).pack(side="right")
        self.texto_resultado = tk.Text(self.panel_derecho, height=7, wrap="word", font=("Segoe UI", 11), bg="#edf7f4", fg="#102a43", state="disabled", relief="flat", padx=10, pady=8)
        self.texto_resultado.pack(fill="both", expand=True, pady=(6, 0))

    def _limpiar_ejemplo_clave(self, _evento):
        if self.entrada_clave.get() == self.ejemplo_clave:
            self.entrada_clave.delete(0, "end")

    def _limpiar_campos(self):
        self.texto_entrada.delete("1.0", "end")
        if self.entrada_clave:
            self.entrada_clave.delete(0, "end")
        self._mostrar_resultado("")

    def _copiar_resultado(self):
        resultado = self.texto_resultado.get("1.0", "end-1c")
        if resultado:
            self.clipboard_clear()
            self.clipboard_append(resultado)

    def _cifrar(self):
        self._ejecutar("cifrar")

    def _descifrar(self):
        self._ejecutar("descifrar")

    def _preparar_clave(self, nombre, clave):
        if nombre in CLAVES_ENTERAS:
            try:
                return int(clave)
            except ValueError as error:
                raise ValueError("La clave debe ser un número entero.") from error
        if nombre == "Transposición por grupos":
            if not clave.isdigit() or sorted(clave) != [str(numero) for numero in range(1, len(clave) + 1)]:
                raise ValueError("Usa una permutación válida, por ejemplo 43521.")
        return clave

    def _preparar_texto(self, nombre, operacion, texto, clave):
        if nombre == "Adición" and operacion == "descifrar":
            partes = [parte for parte in re.split(r"[\s,;]+", texto.strip()) if parte]
            try:
                return [int(parte) for parte in partes]
            except ValueError as error:
                raise ValueError("El mensaje de Adición debe contener números separados por espacios o comas.") from error
        if nombre == "Transposición por columnas" and operacion == "descifrar" and len(texto) % len(clave) != 0:
            raise ValueError("El texto cifrado debe tener una longitud múltiplo de la clave.")
        return texto

    def _ejecutar(self, operacion):
        info = CIFRADOS[self.cifrado_actual]
        texto = self.texto_entrada.get("1.0", "end-1c")
        if not texto.strip():
            messagebox.showwarning("Falta mensaje", "Escribe un mensaje primero.")
            return
        clave = None
        if info["requiere_clave"]:
            clave = self.entrada_clave.get().strip()
            if not clave or clave == self.ejemplo_clave:
                messagebox.showwarning("Falta clave", "Ingresa una clave para este cifrado.")
                return
        try:
            clave = self._preparar_clave(self.cifrado_actual, clave) if clave is not None else None
            texto = self._preparar_texto(self.cifrado_actual, operacion, texto, clave)
            funcion = getattr(info["modulo"], operacion)
            resultado = funcion(texto, clave) if info["requiere_clave"] else funcion(texto)
            if self.cifrado_actual == "Adición" and operacion == "cifrar":
                resultado = " ".join(map(str, resultado))
        except Exception as error:
            messagebox.showerror("No se pudo procesar", str(error))
            return
        self._mostrar_resultado(str(resultado))

    def _mostrar_resultado(self, resultado):
        self.texto_resultado.config(state="normal")
        self.texto_resultado.delete("1.0", "end")
        self.texto_resultado.insert("1.0", resultado)
        self.texto_resultado.config(state="disabled")


def iniciar_app():
    CifradorApp().mainloop()
