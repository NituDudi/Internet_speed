from tkinter import *
import speedtest

# Function to check the internet speed
def check_speed():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down= str(round(sp.download()/(10**6),3))+" Mbps"  # Initiate download test
    up= str(round(sp.upload()/(10**6),3))+" Mbps"# Initiate upload test
    
    lab_down.config(text= down)
    lab_up.config(text= up)

# Setting up the main window
sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x650")
sp.config(bg="Blue")

# Title label
lab = Label(sp, text="Internet Speed Test", font=("Times New Roman", 30, "bold"), bg="Blue", fg="White")
lab.place(x=60, y=40, height=50, width=380)

# Download Speed label and display
lab = Label(sp, text="Download Speed", font=("Times New Roman", 30, "bold"), bg="White", fg="Black")
lab.place(x=60, y=130, height=50, width=380)

lab_down = Label(sp, text="00", font=("Times New Roman", 30, "bold"), bg="White", fg="Black")
lab_down.place(x=60, y=200, height=50, width=380)

# Upload Speed label and display
lab = Label(sp, text="Upload Speed", font=("Times New Roman", 30, "bold"), bg="White", fg="Black")
lab.place(x=60, y=290, height=50, width=380)

lab_up = Label(sp, text="00", font=("Times New Roman", 30, "bold"), bg="White", fg="Black")
lab_up.place(x=60, y=360, height=50, width=380)

# Check Speed Button
button = Button(sp, text="CHECK SPEED", font=("Times New Roman", 30, "bold"), relief=RAISED, bg="Red", fg="Black", command=check_speed())
button.place(x=60, y=460, height=50, width=380)

sp.mainloop()