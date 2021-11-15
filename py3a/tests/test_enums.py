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
