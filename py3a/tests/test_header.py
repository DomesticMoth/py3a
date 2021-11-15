from py3a import Header, ColorMod, DEFAULT_DELAY, DEFAULT_LOOP, DEFAULT_COLORS, DEFAULT_UTF8, DEFAULT_PREVIEW

def test_header_to_string_all_params():
    header = Header(
        width = 1,
        height = 2,
        delay = DEFAULT_DELAY+1,
        loop_enable = not DEFAULT_LOOP,
        color_mod = ColorMod.full,
        utf8 = True,
        datacols = 123,
        preview = 1,
        audio = "1234567",
        title = None,
        author = None,
    )
    s_ref = "width 1\nheight 2\ndelay 51\nloop false\ncolors full\nutf8\ndatacols 123\npreview 1\naudio 1234567\n\n"
    assert header.to_string() == s_ref

def test_header_to_string_default_params():
    header = Header(
        width = 1,
        height = 2,
        delay = DEFAULT_DELAY,
        loop_enable = DEFAULT_LOOP,
        color_mod = DEFAULT_COLORS,
        utf8 = DEFAULT_UTF8,
        datacols = DEFAULT_COLORS.to_datacols(),
        preview = DEFAULT_PREVIEW,
        audio = None,
        title = None,
        author = None,
    )
    s_ref = "width 1\nheight 2\n\n"
    assert header.to_string() == s_ref

def test_header_to_string_datacols():
    header = Header(
        width = 1,
        height = 2,
        delay = DEFAULT_DELAY,
        loop_enable = DEFAULT_LOOP,
        color_mod = DEFAULT_COLORS,
        utf8 = DEFAULT_UTF8,
        datacols = DEFAULT_COLORS.to_datacols()+1,
        preview = DEFAULT_PREVIEW,
        audio = None,
        title = None,
        author = None,
    )
    s_ref = "width 1\nheight 2\ndatacols 2\n\n"
    assert header.to_string() == s_ref

def test_header_from_string_full():
    s = "width 1\nheight 2\ndelay 3\nloop false\ncolors full\nutf8\ndatacols 5\npreview 1\naudio 12345"
    refernce = Header(
        width = 1,
        height = 2,
        delay = 3,
        loop_enable = False,
        color_mod = ColorMod.full,
        utf8 = True,
        datacols = 5,
        preview = 1,
        audio = "12345",
        title = None,
        author = None,
    )
    assert refernce.to_string() == Header.from_string(s).to_string()

def test_header_from_string_only_required():
    s = "width 1\nheight 2"
    refernce = Header(
        width = 1,
        height = 2,
        delay = 50,
        loop_enable = True,
        color_mod = ColorMod.none,
        utf8 = False,
        datacols = 1,
        preview = 0,
        audio = None,
        title = None,
        author = None,
    )
    assert refernce.to_string() == Header.from_string(s).to_string()

def test_header_from_string_optional_incorrect():
    s = "width 1\nheight 2\ndelay safdsfsdf\nloop dsfsdf\ncolors dfdfdf\ndatacols dfsfsddf"
    refernce = Header(
        width = 1,
        height = 2,
        delay = 50,
        loop_enable = True,
        color_mod = ColorMod.none,
        utf8 = False,
        datacols = 1,
        preview = 0,
        audio = None,
        title = None,
        author = None,
    )
    assert refernce.to_string() == Header.from_string(s).to_string()

def test_header_from_string_width_incorrect():
    s = "width sdfsfsdf\nheight 2\ndelay 3\nloop false\ncolors full\nutf8\ndatacols 5\naudio 12345"
    try:
        Header.from_string(s)
        assert False
    except:
        assert True

def test_header_from_string_datacols():
    s = "width 1\nheight 2\ncolors full"
    refernce = Header(
        width = 1,
        height = 2,
        delay = 50,
        loop_enable = True,
        color_mod = ColorMod.full,
        utf8 = False,
        datacols = 3,
        preview = 0,
        audio = None,
        title = None,
        author = None,
    )
    assert refernce.to_string() == Header.from_string(s).to_string()
    s = "width 1\nheight 2\ncolors full\ndatacols 0"
    refernce = Header(
        width = 1,
        height = 2,
        delay = 50,
        loop_enable = True,
        color_mod = ColorMod.full,
        utf8 = False,
        datacols = 0,
        preview = 0,
        audio = None,
        title = None,
        author = None,
    )
    assert refernce.to_string() == Header.from_string(s).to_string()

def test_header_from_string_extra_spaces():
    s = "width    1\nheight    2\ndelay    3\nloop    false\ncolors    full \nutf8   \ndatacols    5\naudio    12345"
    refernce = Header(
        width = 1,
        height = 2,
        delay = 3,
        loop_enable = False,
        color_mod = ColorMod.full,
        utf8 = True,
        datacols = 5,
        preview = 0,
        audio = "12345",
        title = None,
        author = None,
    )
    assert refernce.to_string() == Header.from_string(s).to_string()
