import customtkinter as ctk
from tkinter import messagebox
import pyperclip # Install: pip install pyperclip

class CortexEngine:
    @staticmethod
    def encode(carrier, secret):
        # Pretvaramo tajnu poruku u binarni niz
        binary_secret = ''.join(format(ord(c), '08b') for c in secret)
        # Mapiramo 0 -> \u200b i 1 -> \u200c
        hidden_bits = binary_secret.replace('0', '\u200b').replace('1', '\u200c')
        
        # Ubacujemo nevidljive bitove na početak carrier teksta
        # (Može se modifikovati da se širi kroz ceo tekst)
        return hidden_bits + carrier

    @staticmethod
    def decode(text):
        extracted_bits = ""
        for char in text:
            if char == '\u200b': extracted_bits += '0'
            elif char == '\u200c': extracted_bits += '1'
        
        if not extracted_bits: return None
        
        # Pretvaramo binarno nazad u tekst (8 po 8 bita)
        try:
            chars = [chr(int(extracted_bits[i:i+8], 2)) for i in range(0, len(extracted_bits), 8)]
            return "".join(chars)
        except:
            return None

class CortexApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CORTEX - LINGUISTIC STEALTH")
        self.geometry("900x700")
        ctk.set_appearance_mode("dark")
        
        self.setup_ui()

    def setup_ui(self):
        self.grid_columnconfigure(0, weight=1)
        
        # Header
        self.header = ctk.CTkLabel(self, text="CORTEX ENGINE v1.0", font=("Impact", 35), text_color="#00ff41")
        self.header.pack(pady=20)

        # Carrier Input (Javna poruka)
        self.label1 = ctk.CTkLabel(self, text="COVER TEXT (What everyone sees):", font=("System", 12, "bold"))
        self.label1.pack(anchor="w", padx=40)
        self.cover_text = ctk.CTkTextbox(self, height=150, fg_color="#0a0a0a", border_color="#1a1a1a", border_width=1)
        self.cover_text.pack(fill="x", padx=40, pady=(0, 20))

        # Secret Input (Tajna poruka)
        self.label2 = ctk.CTkLabel(self, text="SECRET MESSAGE (To be hidden):", font=("System", 12, "bold"), text_color="cyan")
        self.label2.pack(anchor="w", padx=40)
        self.secret_text = ctk.CTkEntry(self, height=45, fg_color="#0a0a0a", border_color="cyan", placeholder_text="Enter secret here...")
        self.secret_text.pack(fill="x", padx=40, pady=(0, 20))

        # Buttons
        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.pack(pady=10)

        self.enc_btn = ctk.CTkButton(self.btn_frame, text="ENCODE & COPY", fg_color="#1b5e20", width=200, height=50, font=("System", 14, "bold"), command=self.handle_encode)
        self.enc_btn.grid(row=0, column=0, padx=10)

        self.dec_btn = ctk.CTkButton(self.btn_frame, text="DECODE FROM CLIPBOARD", fg_color="#0d47a1", width=200, height=50, font=("System", 14, "bold"), command=self.handle_decode)
        self.dec_btn.grid(row=0, column=1, padx=10)

        # Output / Status
        self.status_label = ctk.CTkLabel(self, text="SYSTEM READY", font=("Consolas", 12), text_color="#555")
        self.status_label.pack(pady=20)

    def handle_encode(self):
        cover = self.cover_text.get("1.0", "end-1c")
        secret = self.secret_text.get()
        
        if not cover or not secret:
            messagebox.showerror("Error", "Both fields are required!")
            return
            
        encoded = CortexEngine.encode(cover, secret)
        pyperclip.copy(encoded)
        self.status_label.configure(text="SUCCESS: Encoded text copied to clipboard!", text_color="#00ff41")
        self.secret_text.delete(0, 'end')

    def handle_decode(self):
        clipboard = pyperclip.paste()
        decoded = CortexEngine.decode(clipboard)
        
        if decoded:
            messagebox.showinfo("CORTEX - Decoded Message", f"Found hidden message:\n\n{decoded}")
            self.status_label.configure(text=f"Last decoded: {decoded}", text_color="cyan")
        else:
            messagebox.showerror("Error", "No hidden message found in clipboard!")

if __name__ == "__main__":
    app = CortexApp()
    app.mainloop()
