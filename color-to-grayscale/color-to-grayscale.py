def color_to_grayscale(image):
    height = len(image)
    width = len(image[0])

    gray = []

    for i in range(height):
        row = []
        for j in range(width):
            r, g, b = image[i][j]
            gray_value = 0.299*r + 0.587*g + 0.114*b
            row.append(gray_value)
        gray.append(row)

    return gray
