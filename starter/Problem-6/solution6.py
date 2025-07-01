def isLandscape(height, width):
    if width > height:
        return "Landscape"
    else:
        return "Portrait"
    

print(isLandscape(1080, 1920))  # Landscape