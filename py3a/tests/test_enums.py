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
from py3a import ColorMod, Color


def convertable_enum_testing(enum_class, strings):
    for string in strings:
        assert string == str(enum_class.fromstr(string))

def test_color_mod():
    strings = [ 'none', 'fg', 'bg', 'full' ]
    convertable_enum_testing(ColorMod, strings)

def test_color():
    strings = [ 
        '0', 
        '1', 
        '2', 
        '3', 
        '4', 
        '5', 
        '6', 
        '7', 
        '8', 
        '9', 
        'a', 
        'b', 
        'c', 
        'd', 
        'e', 
        'f'
    ]
    convertable_enum_testing(Color, strings)
