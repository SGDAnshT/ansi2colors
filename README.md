Convert ANSI-colored ASCII art into Python source code.

Perfect for projects using custom classes (defaults to `Colors.*`), Colorama, Rich, or other terminal color libraries.

- Parses ANSI true color escapes
- Converts ANSI art into Python strings
- Supports custom palettes
- Useful for optimization

I personally used this with "ascii-image-converter" with the -C / --color flag 
(see https://github.com/TheZoraiz/ascii-image-converter)
Syntax - ascii-image-converter [filename.png] -C > logo.ansi