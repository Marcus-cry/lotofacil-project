import random
import threading
import time
import tkinter as tk

GL_HEIGHT = 400
GL_WIDTH = 400

class LotofacilGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Globo Lotofácil")
        self.geometry(f"{GL_WIDTH}x{GL_HEIGHT+100}")

        self.canvas = tk.Canvas(self, width=GL_WIDTH, height=GL_HEIGHT, bg="#fafafa")
        self.canvas.pack()
        self.status = tk.Label(self, text="Pronto para sortear", font=("Arial", 16))
        self.status.pack(pady=10)
        self.btn = tk.Button(self, text="Sortear 15 bolas", command=self.start_draw)
        self.btn.pack()

        self.draw_globe([])

    def draw_globe(self, nums):
        self.canvas.delete("all")
        pad = 20
        self.canvas.create_oval(pad, pad, GL_WIDTH-pad, GL_HEIGHT-pad, outline="#444", width=3)
        text = " ".join(f"{n:02d}" for n in sorted(nums))
        self.canvas.create_text(GL_WIDTH/2, GL_HEIGHT/2, text=text, font=("Courier", 14))

    def start_draw(self):
        self.btn.config(state="disabled")
        threading.Thread(target=self.perform_draw, daemon=True).start()

    def perform_draw(self):
        pool = list(range(1, 26))
        random.shuffle(pool)
        sorteados = []
        for _ in range(15):
            num = pool.pop()
            sorteados.append(num)
            self.status.config(text=f"Bola sorteada: {num:02d}")
            self.draw_globe(sorteados)
            time.sleep(1)
        self.status.config(text="Sorteio concluído")
        self.btn.config(state="normal")

if __name__ == "__main__":
    LotofacilGUI().mainloop()
