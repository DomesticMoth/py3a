# py3a
This library provides a structural representation of [3a ascii animations format](https://github.com/DomesticMoth/3a) and methods for reading and writing it.  
This lib on [pypi](https://pypi.org/project/py3a) 
- [Usage](#usage)
- [Short API description](#short-api-description)
  - [Structs](#structs)
  - [Functions](#functions)
## Usage
Install  
```
$ pip install py3a
```
Here's a simple example that parsing a string in 3a format and displaying a header:  
```python
import py3a

COLORTABLE_EXAMPLE = """	
width 32
height 19
loop false
colors full
title colortable demo
author Moth

in ' ab '                       ffffffffffffffffffffffffffffffff00000000000000000000000000000000
a-foreground, b-background      ffffffffffffffffffffffffffffffff00000000000000000000000000000000
                                ffffffffffffffffffffffffffffffff00000000000000000000000000000000
 00  01  02  03  04  05  06  07 0000000000000000000000000000000000001111222233334444555566667777
 10  11  12  13  14  15  16  17 1111111111111111111111111111111100001111222233334444555566667777
 20  21  22  23  24  25  26  27 2222222222222222222222222222222200001111222233334444555566667777
 30  31  32  33  34  35  36  37 3333333333333333333333333333333300001111222233334444555566667777
 40  41  42  43  44  45  46  47 4444444444444444444444444444444400001111222233334444555566667777
 50  51  52  53  54  55  56  57 5555555555555555555555555555555500001111222233334444555566667777
 60  61  62  63  64  65  66  67 6666666666666666666666666666666600001111222233334444555566667777
 70  71  72  73  74  75  76  77 7777777777777777777777777777777700001111222233334444555566667777
 80  81  82  83  84  85  86  87 8888888888888888888888888888888800001111222233334444555566667777
 90  91  92  93  94  95  96  97 9999999999999999999999999999999900001111222233334444555566667777
 a0  a1  a2  a3  a4  a5  a6  a7 aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa00001111222233334444555566667777
 b0  b1  b2  b3  b4  b5  b6  b7 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb00001111222233334444555566667777
 c0  c1  c2  c3  c4  c5  c6  c7 cccccccccccccccccccccccccccccccc00001111222233334444555566667777
 d0  d1  d2  d3  d4  d5  d6  d7 dddddddddddddddddddddddddddddddd00001111222233334444555566667777
 e0  e1  e2  e3  e4  e5  e6  e7 eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee00001111222233334444555566667777
 f0  f1  f2  f3  f4  f5  f6  f7 ffffffffffffffffffffffffffffffff00001111222233334444555566667777"""


if __name__ == "__main__":
    art = py3a.Art.load(COLORTABLE_EXAMPLE)
    print(art.header)
```
## Short API description
### Classes
The core of the library is the Art class, which implements the 3a structure:  
```python
class Art:
    def __init__ (self, header: Header, body: Body):
        self.header = header
        self.body = body
```
Header type contains information about the header of 3a file:  
```python
class Header:
    def __init__ (self, width: int, height: int, delay: int, loop_enable: bool, color_mod: ColorMod,
                    utf8: bool, datacols: int, preview: int, audio: str, title: str, author: str):
        self.width = width
        self.height = height
        self.delay = delay
        self.loop_enable = loop_enable
        self.color_mod = color_mod
        self.utf8 = utf8
        self.datacols = datacols
        self.preview = preview
        self.audio = audio
        self.title = title
        self.author = author
```
Body class contains a list of frames, where each frame is a list of rows, and each row is a list of row fragments:  
```python
Row = typing.List[RowFragment]

Frame = typing.List[Row]

class Body:
    def __init__ (self, frames: typing.List[Frame] ):
        self.frames = frames
```
Each RowFragment is a set of consecutive symbols with the same values of foreground and background colors:  
```python
class RowFragment:
    def __init__ (self, text: str, fg_color: Color, bg_color: Color):
        self.text = text
        self.fg_color = fg_color
        self.bg_color = bg_color
```
### Methods
`Art.load` and `art.save` methods allow you to convert strings to `Art` and back.  
`Art.load_file` and `art.save_file` methods allow you to read 3a files to `Art` and write `Art` to 3a files.  
