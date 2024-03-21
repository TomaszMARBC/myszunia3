import tkinter as tk
from PIL import Image, ImageTk
import PoC_main as myszunia


if __name__ == '__main__':
    root = tk.Tk()
    
    canvas = tk.Canvas(root, width=1200, height=400)
    canvas.grid(columnspan=3, rowspan=4)
    
    logo = Image.open("logo.png")
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image=logo)
    logo_label.image = logo
    logo_label.grid(column=1, row=0)
    
    instructions = tk.Label(root, text='Witamy w Proof of Concept BDSM\n\nWpisz wartości testowe dla myszki w poszczególne pola.')
    instructions.grid(columnspan=3, column=0, row=1)
    
    def start_test():
        
        text_box = tk.Text(root, height=10, width=100, padx=15, pady=15)
        text_box.insert(1.0, 'test text boxa')
        text_box.grid(column=1, row=3)
        print('Test rozpocząty')
    
    browse_text = tk.StringVar()
    browse_btn = tk.Button(root, textvariable=browse_text, command=lambda: start_test(), bg="#D02602", height=2, width=20)
    browse_text.set('START TEST')
    browse_btn.grid(column=1, row=2)
    
    canvas = tk.Canvas(root, width=1200, height=200)
    canvas.grid(columnspan=3)
    
    root.mainloop()
