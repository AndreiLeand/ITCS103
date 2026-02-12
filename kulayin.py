def rainbow(label):
    colors = ["#FF0000","#6dd5ed","#0000FF","#6dd5ed","#800080","#6dd5ed"]
    i = 0

    def change_color():
        nonlocal i
        label.config(fg=colors[i])
        i = (i + 1) % len(colors)
        label.after(500, change_color)

    change_color()