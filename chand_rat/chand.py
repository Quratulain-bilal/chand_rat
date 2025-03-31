from turtle import *
import time

# Set up screen with maximum speed
speed(0)
tracer(20)
bgcolor("black")
setup(width=900, height=800)
title("Chand Raat Mubarak")

# Add this code to center the window
canvas = getcanvas()
root = canvas.winfo_toplevel()
root.update_idletasks()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 900
window_height = 800
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Rest of your original code remains exactly the same
colors = ['white', 'orange']
for i in range(205):
    color(colors[i % 2])
    rt(i)
    circle(200, i + 2)
    fd(i)
    right(180)
    fd(i)
    update()

tracer(0)

def write_text(message, x, y, size, color_text, font_style="Arial"):
    penup()
    goto(x, y)
    color(color_text)
    style = (font_style, size, "bold")
    write(message, font=style, align="center")

write_text("✨ Chand Rat Mubarik✨", 0, 220, 45, "#FFA500", "Nazafat Nastaleeq")

colors = ['#FFD700', '#FFA500', '#FFFFFF', '#FF4500']
for i in range(200):
    color(colors[i % len(colors)])
    rt(i)
    circle(180, i + 2)
    fd(i)
    right(180)
    fd(i)
    update()

def draw_moon(x, y):
    penup()
    goto(x, y)
    pendown()
    color("#FFFFE0")
    begin_fill()
    circle(50)
    end_fill()

draw_moon(120, 50)

def draw_star(x, y, size):
    penup()
    goto(x, y)
    pendown()
    color("white")
    begin_fill()
    for _ in range(5):
        forward(size)
        right(144)
    end_fill()

star_positions = [(-180, 100), (-100, 130), (0, 110), (80, 140), 
                 (150, 120), (-150, 30), (200, 70), (-200, 70)]
for x, y in star_positions:
    draw_star(x, y, 20)

write_text('﴿وَٱعْبُدْ رَبَّكَ حَتَّىٰ يَأْتِيَكَ ٱلْيَقِينُ﴾', 0, -180, 30, "#FFFFFF", "Traditional Arabic")
write_text('"And worship your Lord until certainty comes to you."', 0, -220, 18, "#FFA500", "Arial")
write_text('"اور اپنے رب کی عبادت کرتے رہو یہاں تک کہ تمہیں یقین (موت) آجائے۔"', 0, -250, 22, "#FFFFFF", "Nafees Nastaleeq")

color("#FF4500")
penup()
goto(-350, -280)
pendown()
width(3)
for _ in range(2):
    forward(700)
    left(90)
    forward(5)
    left(90)

hideturtle()
done()