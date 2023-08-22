def convert_pixel_to_char(pixel):
    ascii_chars = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']
    intensity = pixel / 255
    index = int(intensity * len(ascii_chars) - 1)
    return ascii_chars[index]


def generate_ascii_art(image_path, width, height):
    from PIL import Image

    image = Image.open(image_path)
    image = image.resize((width, height))
    image = image.convert('L')

    ascii_art = ''
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            char = convert_pixel_to_char(pixel)
            ascii_art += char
        ascii_art += '\n'

    return ascii_art


def main():
    image_path = './image.jpg'
    width = 80
    height = 40

    ascii_art = generate_ascii_art(image_path, width, height)
    print(ascii_art)


if __name__ == '__main__':
    main()
