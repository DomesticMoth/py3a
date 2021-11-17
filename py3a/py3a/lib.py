"""
    This file is part of pu3a.

    py3a is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    py3a is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with py3a.  If not, see <https://www.gnu.org/licenses/>.
"""
from .enums import ColorMod, Color
from .errors import *
import typing
import re
import json


DEFAULT_DELAY = 50
DEFAULT_PREVIEW = 0
DEFAULT_LOOP = True
DEFAULT_COLORS = ColorMod.none
DEFAULT_UTF8 = False


def remove_comments(s: str) -> str:
    s = re.sub(r"(?m)^\t.*?(\n|$)", "", s)
    s = re.sub(r"\t.*?(\n|$)", "\n", s)
    return s

def only_payload(v):
    ret = []
    for s in v:
        if s != "":
            ret.append(s)
    return ret

class RowFragment:
    def __init__ (self, text: str, fg_color: Color, bg_color: Color):
        self.text = text
        self.fg_color = fg_color
        self.bg_color = bg_color

Row = typing.List[RowFragment]

Frame = typing.List[Row]

def generate_color_fragment(color: Color, count: int) -> str:
    ret = ""
    if color is not None:
        c = str(color)
        ret += c*count
    return ret


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

    def __str__(self) -> str:
        d = {
            "width": self.width,
            "height": self.height,
            "delay": self.delay,
            "loop_enable": self.loop_enable,
            "color_mod": str(self.color_mod),
            "utf8": self.utf8,
            "datacols": self.datacols,
            "preview": self.preview,
            "audio": self.audio,
            "title": self.title,
            "author": self.author
        }
        return json.dumps(d, indent=2)
        
    @classmethod
    def from_string(cls, s: str):
        width = 0
        w_set = False;
        height = 0
        h_set = False
        delay = DEFAULT_DELAY
        loop_enable = DEFAULT_LOOP
        color_mod = DEFAULT_COLORS
        utf8 =  DEFAULT_UTF8
        datacols = 0
        d_set = False
        preview = DEFAULT_PREVIEW
        audio = None
        title = None
        author = None
        rows = s.split("\n")
        for row in rows:
            tokens = row.split(" ")
            tokens = only_payload(tokens)
            try:
                if tokens[0] == "width":
                    width = int(tokens[1])
                    w_set = True
                elif tokens[0] == "height":
                    height = int(tokens[1])
                    h_set = True
                elif tokens[0] == "delay":
                    delay = int(tokens[1])
                elif tokens[0] == "loop":
                    if tokens[1] == "true":
                        loop_enable = True
                    if tokens[1] == "false":
                        loop_enable = False
                elif tokens[0] == "colors":
                    color_mod = ColorMod.fromstr(tokens[1])
                elif tokens[0] == "utf8":
                    utf8 = True
                elif tokens[0] == "datacols":
                    datacols = int(tokens[1])
                    d_set = True
                elif tokens[0] == "preview":
                    preview = int(tokens[1])
                elif tokens[0] == "audio":
                    if tokens[1] != "":
                        audio = str(tokens[1])
                elif tokens[0] == "title":
                    s = ""
                    for i in range(1, len(tokens)):
                        s += tokens[i]
                    title = s
                elif tokens[0] == "author":
                    s = ""
                    for i in range(1, len(tokens)):
                        s += tokens[i]
                    author = s
            except:
                continue
        if not w_set:
            raise InvalidWidth()
        if not h_set:
            raise InvalidHeight()
        if not d_set:
            datacols = color_mod.to_datacols()
        return cls(width, height, delay, loop_enable, color_mod, utf8, datacols, preview, audio, title, author)

    def to_string(self) -> str:
        ret = ""
        ret += "width "
        ret += str(self.width)
        ret += "\nheight "
        ret += str(self.height)
        if self.delay != DEFAULT_DELAY:
            ret += "\ndelay "
            ret += str(self.delay)
        if self.loop_enable != DEFAULT_LOOP:
            ret += "\nloop "
            if self.loop_enable:
                ret += "true"
            else:
                ret += "false"
        if self.color_mod != DEFAULT_COLORS:
            ret += "\ncolors "
            ret += str(self.color_mod)
        if self.utf8:
            ret += "\nutf8"
        if self.color_mod.to_datacols() != self.datacols:
            ret += "\ndatacols "
            ret += str(self.datacols)
        if self.preview != DEFAULT_PREVIEW:
            ret += "\npreview "
            ret += str(self.preview)
        if self.audio is not None:
            ret += "\naudio "
            ret += self.audio
        if self.title is not None:
            ret += "\ntitle "
            ret += self.title
        if self.author is not None:
            ret += "\nauthor "
            ret += self.author
        ret += "\n\n"
        return ret

class Body:
    def __init__ (self, frames: typing.List[Frame] ):
        self.frames = frames

    @classmethod
    def from_string(cls, s: str, h: Header):
        s = re.sub("(\n|\t)", "", s)
        char_vec = [char for char in s]
        length = len(char_vec)
        frm = 0
        width = h.width
        height = h.height
        datacols = h.datacols
        frames = []
        nxt = True
        brk = False
        while nxt:
            frame = []
            for y in range(height):
                row = []
                row_fragment = RowFragment(
                    text = "",
                    fg_color = None,
                    bg_color = None
                )
                for x in range(width):
                    symbol_pos = (frm*width*datacols*height)+(y*width*datacols)+x
                    if symbol_pos >= length:
                        nxt = False
                        break
                    symbol = char_vec[symbol_pos]
                    fg_color = None
                    bg_color = None
                    if h.color_mod == ColorMod.fg:
                        fg_color_position = (frm*width*datacols*height)+(y*width*datacols)+width+x
                        if fg_color_position >= length:
                            nxt = False
                            break
                        fg_color = Color.fromstr(char_vec[fg_color_position])
                    elif h.color_mod == ColorMod.bg:
                        bg_color_position = (frm*width*datacols*height)+(y*width*datacols)+width+x
                        if bg_color_position >= length:
                            nxt = False
                            break
                        bg_color = Color.fromstr(char_vec[bg_color_position])
                    elif h.color_mod == ColorMod.full:
                        fg_color_position = (frm*width*datacols*height)+(y*width*datacols)+width+x
                        bg_color_position = (frm*width*datacols*height)+(y*width*datacols)+width*2+x
                        if fg_color_position >= length or bg_color_position >= length:
                            nxt = false
                            break
                        fg_color = Color.fromstr(char_vec[fg_color_position])
                        bg_color = Color.fromstr(char_vec[bg_color_position])
                    if x == 0:
                        row_fragment.fg_color = fg_color
                        row_fragment.bg_color = bg_color
                    else:
                        if row_fragment.fg_color != fg_color or row_fragment.bg_color != bg_color:
                            row.append(row_fragment)
                            row_fragment = RowFragment(
                                text = symbol,
                                fg_color = fg_color,
                                bg_color = bg_color,
                            )
                            continue
                    row_fragment.text += symbol
                if len(row_fragment.text) > 0:
                    row.append(row_fragment)
                if len(row) < 1:
                    brk = True
                    break
                frame.append(row)
            if brk:
                break
            frames.append(frame)
            frm += 1;
        return cls(frames)

    def to_string(self, pretify: bool) -> str:
        ret = ""
        for frm, frame in enumerate(self.frames):
            for row in frame:
                text_col = ""
                color1_col = ""
                color2_col = ""
                for fragment in row:
                    text_col += fragment.text
                    color1_col += generate_color_fragment(fragment.fg_color, len(fragment.text))
                    color2_col += generate_color_fragment(fragment.bg_color, len(fragment.text))
                ret += text_col
                ret += color1_col
                ret += color2_col
                if pretify:
                    ret += '\n'
            if frm < len(self.frames)-1:
                ret += '\n'
        return ret

class Art:
    def __init__ (self, header: Header, body: Body):
        self.header = header
        self.body = body

    @classmethod
    def load(cls, s: str):
        s = remove_comments(s)
        fragments = s.split("\n\n", 1)
        if len(fragments) < 2:
            raise ThereIsNoBody()
        header = Header.from_string(fragments[0])
        body = Body.from_string(fragments[1], header)
        return cls(header, body)
    
    def save(self, pretify: bool) -> str:
        return self.header.to_string() + "\n" + self.body.to_string(pretify)

    @classmethod
    def load_file(cls, path: str):
        with open(path, 'r') as f:
            return cls.load(f.readlines())

    def save_file(self, path: str, pretify: bool):
        with open(path, 'w') as f:
            f.write(self.save(pretify))
