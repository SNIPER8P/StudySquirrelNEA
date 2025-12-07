import customtkinter as ctk
from PIL import Image
import loading
import login
import create
import auth

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

    def handle_signup(self):
        username = self.username_entry.get().strip()
        email = self.email_entry.get().strip().lower()
        password = self.password_entry.get().strip()
        confirm_password = self.confirm_entry.get().strip()

        #Validate inputs
        error = auth.checkSignup(username, email, password, confirm_password)
        if error:
            self.feedback.configure(text=error, text_color="red")
            return
        
        #Save user
        try:
            auth.addUser(username, email, password)
            self.clear_signup_form()
            self.feedback.configure(text="Account created successfully!", text_color="green")
        except Exception as e:
            self.feedback.configure(text=f"Error creating account: {str(e)}", text_color="red")

    def clear_signup_form(self):
        for entry in [self.username_entry, self.email_entry, self.password_entry, self.confirm_entry]:
            entry.delete(0, 'end')
    
if __name__ == "__main__":
    app = App()
    app.mainloop()
