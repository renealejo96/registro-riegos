import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime
import os


class RiegosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Riegos - Finca")
        self.root.geometry("800x600")
        
        # Inicializar base de datos
        self.init_database()
        
        # Variables
        self.selected_blocks = {}
        self.tipo_riego_var = tk.StringVar(value="agua")
        
        # Crear interfaz
        self.create_widgets()
        self.load_today_data()
    
    def init_database(self):
        """Inicializa la base de datos SQLite"""
        self.conn = sqlite3.connect('riegos.db')
        self.cursor = self.conn.cursor()
        
        # Crear tabla de riegos
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS riegos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha DATE NOT NULL,
                bloque TEXT NOT NULL,
                tipo_riego TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()
    
    def create_widgets(self):
        """Crea los widgets de la interfaz"""
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Título
        title_label = ttk.Label(main_frame, text="Registro de Riegos", 
                               font=('Arial', 18, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Fecha actual
        fecha_label = ttk.Label(main_frame, 
                               text=f"Fecha: {datetime.now().strftime('%d/%m/%Y')}", 
                               font=('Arial', 12))
        fecha_label.grid(row=1, column=0, columnspan=2, pady=5)
        
        # Frame para tipo de riego
        tipo_frame = ttk.LabelFrame(main_frame, text="Tipo de Riego", padding="10")
        tipo_frame.grid(row=2, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))
        
        ttk.Radiobutton(tipo_frame, text="Riego con Agua", 
                       variable=self.tipo_riego_var, 
                       value="agua").grid(row=0, column=0, padx=10)
        ttk.Radiobutton(tipo_frame, text="Riego por Comida (Fertilizante)", 
                       variable=self.tipo_riego_var, 
                       value="comida").grid(row=0, column=1, padx=10)
        
        # Frame para bloques
        bloques_frame = ttk.LabelFrame(main_frame, text="Seleccionar Bloques", padding="10")
        bloques_frame.grid(row=3, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Crear checkboxes para bloques (ejemplo: Bloque A-J)
        self.bloques = ['Bloque A', 'Bloque B', 'Bloque C', 'Bloque D', 'Bloque E',
                        'Bloque F', 'Bloque G', 'Bloque H', 'Bloque I', 'Bloque J']
        
        for i, bloque in enumerate(self.bloques):
            var = tk.BooleanVar()
            self.selected_blocks[bloque] = var
            row = i // 3
            col = i % 3
            ttk.Checkbutton(bloques_frame, text=bloque, variable=var).grid(
                row=row, column=col, padx=10, pady=5, sticky=tk.W)
        
        # Botones
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=4, column=0, columnspan=2, pady=20)
        
        ttk.Button(button_frame, text="Registrar Riego", 
                  command=self.registrar_riego).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Ver Historial", 
                  command=self.ver_historial).grid(row=0, column=1, padx=5)
        ttk.Button(button_frame, text="Limpiar Selección", 
                  command=self.limpiar_seleccion).grid(row=0, column=2, padx=5)
        
        # Frame para mostrar registros del día
        historial_frame = ttk.LabelFrame(main_frame, text="Registros de Hoy", padding="10")
        historial_frame.grid(row=5, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Treeview para mostrar registros
        columns = ('Hora', 'Bloque', 'Tipo de Riego')
        self.tree = ttk.Treeview(historial_frame, columns=columns, show='headings', height=8)
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)
        
        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(historial_frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Configurar pesos para que sea responsivo
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(5, weight=1)
    
    def registrar_riego(self):
        """Registra los riegos seleccionados en la base de datos"""
        bloques_seleccionados = [bloque for bloque, var in self.selected_blocks.items() 
                                if var.get()]
        
        if not bloques_seleccionados:
            messagebox.showwarning("Advertencia", 
                                  "Por favor seleccione al menos un bloque")
            return
        
        tipo_riego = self.tipo_riego_var.get()
        fecha_hoy = datetime.now().strftime('%Y-%m-%d')
        
        try:
            for bloque in bloques_seleccionados:
                self.cursor.execute('''
                    INSERT INTO riegos (fecha, bloque, tipo_riego)
                    VALUES (?, ?, ?)
                ''', (fecha_hoy, bloque, tipo_riego))
            
            self.conn.commit()
            
            tipo_texto = "Agua" if tipo_riego == "agua" else "Comida (Fertilizante)"
            messagebox.showinfo("Éxito", 
                              f"Riego registrado correctamente\n" +
                              f"Bloques: {', '.join(bloques_seleccionados)}\n" +
                              f"Tipo: {tipo_texto}")
            
            self.limpiar_seleccion()
            self.load_today_data()
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al registrar: {str(e)}")
    
    def load_today_data(self):
        """Carga los datos del día actual en el treeview"""
        # Limpiar treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        fecha_hoy = datetime.now().strftime('%Y-%m-%d')
        
        self.cursor.execute('''
            SELECT timestamp, bloque, tipo_riego 
            FROM riegos 
            WHERE fecha = ?
            ORDER BY timestamp DESC
        ''', (fecha_hoy,))
        
        registros = self.cursor.fetchall()
        
        for registro in registros:
            timestamp, bloque, tipo_riego = registro
            hora = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S').strftime('%H:%M:%S')
            tipo_texto = "Agua" if tipo_riego == "agua" else "Comida (Fertilizante)"
            self.tree.insert('', 0, values=(hora, bloque, tipo_texto))
    
    def ver_historial(self):
        """Abre una ventana con el historial completo"""
        historial_window = tk.Toplevel(self.root)
        historial_window.title("Historial de Riegos")
        historial_window.geometry("700x500")
        
        # Frame principal
        frame = ttk.Frame(historial_window, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Treeview
        columns = ('Fecha', 'Hora', 'Bloque', 'Tipo de Riego')
        tree = ttk.Treeview(frame, columns=columns, show='headings', height=20)
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150)
        
        tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        tree.configure(yscrollcommand=scrollbar.set)
        
        # Cargar datos
        self.cursor.execute('''
            SELECT fecha, timestamp, bloque, tipo_riego 
            FROM riegos 
            ORDER BY timestamp DESC
        ''')
        
        registros = self.cursor.fetchall()
        
        for registro in registros:
            fecha, timestamp, bloque, tipo_riego = registro
            fecha_format = datetime.strptime(fecha, '%Y-%m-%d').strftime('%d/%m/%Y')
            hora = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S').strftime('%H:%M:%S')
            tipo_texto = "Agua" if tipo_riego == "agua" else "Comida (Fertilizante)"
            tree.insert('', tk.END, values=(fecha_format, hora, bloque, tipo_texto))
        
        # Configurar pesos
        historial_window.columnconfigure(0, weight=1)
        historial_window.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)
    
    def limpiar_seleccion(self):
        """Limpia la selección de bloques"""
        for var in self.selected_blocks.values():
            var.set(False)
    
    def __del__(self):
        """Cierra la conexión a la base de datos al cerrar la aplicación"""
        if hasattr(self, 'conn'):
            self.conn.close()


def main():
    root = tk.Tk()
    app = RiegosApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()