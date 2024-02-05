import tkinter as tk 
from tkinter import ttk

class View(tk.Tk):
    
    PAD = 10 
    MAX_BUTTONS_PER_ROW = 4
    
    button_captions = [
        'Show available IoT', 'connect IoT', 'delete list'
    ]
    
    def __init__(self,controller):
        
        super().__init__()
        
        self.valueVar = tk.StringVar()
        
        self.title("IoT app 0.1")
        self.controller = controller
        
        self.available_IoTs = []
        
        self._make_main_frame()
        
        self._make_buttons()
        self._make_list()
        
        self._center_window()
    
    # ================================================================== #  
    # ======================== INITIAL FUNCTIONS ======================= #  
    # ================================================================== #  
        
    def main(self):
        self.mainloop()
        
    def _make_main_frame(self):

        self.main_frm = ttk.Frame(self)
        self.main_frm.pack()
    
    def _center_window(self):
        self.update()
        width = self.winfo_width()
        height = self.winfo_height()
        
        x_offset = (self.winfo_screenwidth() - width) // 3
        y_offset = (self.winfo_screenheight()- height) // 3
        
        self.geometry(f'400x400+{x_offset}+{y_offset}')
        
    # ================================================================== #  
    # ======================= BUTTONS MANAGEMENT ======================= #  
    # ================================================================== #    
    
    def _make_buttons(self):
        
        outer_frm = ttk.Frame(self.main_frm)
        outer_frm.pack()
    
        frm = ttk.Frame(outer_frm)
        frm.pack()
        
        buttons_in_row = 0
        
        for caption in self.button_captions:
            if buttons_in_row == self.MAX_BUTTONS_PER_ROW:
                frm = ttk.Frame(outer_frm)
                frm.pack()
                buttons_in_row = 0
                
            btn = ttk.Button(
                            frm,
                            text = caption,
                            command = (lambda button = caption: self.controller.show_available_iot(button))
                            )
                            
            btn.pack()
            
            buttons_in_row += 1
            
    # ================================================================== #
    # ========================= LIST MANAGEMENT ======================== #    
    # ================================================================== #  
    
    def _make_list(self):
        self.lst = tk.Listbox(self)
        self.lst.pack()    
        
    def update_list(self):
        cpt = 0
        
        self.lst.delete(0,tk.END)
        
        for item in self.available_IoTs: 
            self.lst.insert(cpt,item)
            cpt += 1
            
        self.lst.pack()
        
    def delete_list(self):
        self.lst.delete(0,tk.END)