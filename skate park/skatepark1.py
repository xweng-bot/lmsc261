skateboard_colors = {}
i = 0

while i < 4:
    print(i)
    

    name = input(f"Enter the name of skater {i}:")

    color = input("Enter the color of the skateboard:")
    skateboard_colors[name] = color
    i += 1

print(skateboard_colors)