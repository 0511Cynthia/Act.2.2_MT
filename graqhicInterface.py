import tkinter as tk
from turingMachine import TuringMachine

class TmInterfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Máquina de Turing - Verificación de Cadena")
        self.root.geometry("400x300")
        self.root.configure(bg="#a86fc9")

        self.title_label = tk.Label(
            root, text="Máquina de Turing", font=("Helvetica", 20, "bold"), bg="#a86fc9", fg="#2d0933"
        )
        self.title_label.pack(pady=20)

        self.label = tk.Label(
            root, text="Escribe la cadena que se analizará:",
            font=("Helvetica", 12), bg="#a86fc9", fg="#f0e3ff"
        )
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Helvetica", 12), bg="#e8d8f7", fg="#4d003f")
        self.entry.pack(pady=10)

        self.verify_button = tk.Button(
            root, text="Verificar", font=("Helvetica", 12, "bold"), bg="#b44f9f", fg="white",
            relief="flat", padx=10, pady=5, command=self.verify_string
        )
        self.verify_button.pack(pady=20)

        self.result_label = tk.Label(
            root, text="", font=("Helvetica", 12), bg="#a86fc9", fg="#f0e3ff"
        )
        self.result_label.pack(pady=10)

    def verify_string(self):
        input_string = self.entry.get().strip()

        if not input_string.isdigit() or any(c not in '01' for c in input_string):
            self.show_popup("Error: La cadena debe contener solo caracteres binarios (0 y 1)", "Error", "#e74c3c")
            return

        try:
            tm = TuringMachine(list(input_string))
            result, total_sum = tm.run()
            
            if result:
                binary_result = bin(total_sum)[2:]
                self.show_popup(f"Suma: {total_sum} - Binario: {binary_result}", "Resultado", "#2ecc71")
            else:
                self.show_popup("¡Cadena inválida!", "Resultado", "#9d2020")
        
        except Exception as e:
            self.show_popup(f"Error: {str(e)}", "Error", "#9d2020")

    def show_popup(self, message, title, color):
        popup = tk.Toplevel(self.root)
        popup.title(title)
        popup.geometry("300x150")
        popup.configure(bg="#a86fc9")

        label = tk.Label(
            popup, text=message, font=("Helvetica", 12, "bold"), bg="#a86fc9", fg=color
        )
        label.pack(pady=20)

        close_button = tk.Button(
            popup, text="Cerrar", font=("Helvetica", 12, "bold"), bg="#b44f9f", fg="white",
            relief="flat", padx=10, pady=5, command=popup.destroy
        )
        close_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = TmInterfaz(root)
    root.mainloop()