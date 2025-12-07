import customtkinter as ctk
from PIL import Image
import loading
import login
import create

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Study Squirrel")
        self.geometry("1920x1080")
        self.resizable(False, False)
        self.attributes("-fullscreen", True)
        self.configure(fg_color="#DDD5C9")

        self.logoImage = ctk.CTkImage(Image.open("logo.png"), size=(150,150))
        self.loadingImage = ctk.CTkImage(Image.open("logo.png"), size=(500,500))
        self.sideImage = ctk.CTkImage(Image.open("side.png"), size=(250,400))

        self.loadingFrame = loading.loadingFrame(self)
        self.loginFrame = login.loginFrame(self)
        self.createFrame = create.createFrame(self)

        self.show_frame(self.loadingFrame)
        self.run_progress()

    def show_frame(self, frame):
        if hasattr(self, "current_frame"):
            self.current_frame.place_forget()
        self.current_frame = frame
        self.current_frame.place(x=0, y=0)

    def run_progress(self):
        import time
        for i in range(101):
            self.loading_progress.set(i / 100)
            self.update()
            time.sleep(0.015)
        else:
            self.show_frame(self.loginFrame)

    
if __name__ == "__main__":
    app = App()
    app.mainloop()