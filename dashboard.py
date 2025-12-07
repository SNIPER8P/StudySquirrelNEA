import customtkinter as ctk

def dashboardFrame(app):
    frame = ctk.CTkFrame(app, fg_color="#DDD5C9", width=1920, height=1080)
    
    logo_label = ctk.CTkLabel(frame, image=app.logoImage, text="")
    logo_label.place(x=20, y=1000, anchor="center")


    return frame
