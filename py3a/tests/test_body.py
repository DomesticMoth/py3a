from py3a import Body, RowFragment, Color, Header, DEFAULT_PREVIEW, ColorMod


def test_body_to_text_correct_fullcolor():
    text_reference = "AAAAaabb1122\nBBBBaabc1122\nCCCCaaaa1111\nDDDDabcd1111\n\nAAAAaabb1122\nBBBBaabc1122\nCCCCaaaa1111\nDDDDabcd1111\n"
    body = Body(
        frames = [
            [
                [
                    RowFragment(
                        text = "AA",
                        bg_color = Color.BLUE,
                        fg_color = Color.BRIGHT_GREEN,
                    ),
                    RowFragment(
                        text = "AA",
                        bg_color = Color.GREEN,
                        fg_color = Color.BRIGHT_CYAN,
                    ),
                ],
                [
                    RowFragment(
                        text = "BB",
                        bg_color = Color.BLUE,
                        fg_color = Color.BRIGHT_GREEN,
                    ),
                    RowFragment(
                        text = "B",
                        bg_color = Color.GREEN,
                        fg_color = Color.BRIGHT_CYAN,
                    ),
                    RowFragment(
                        text = "B",
                        bg_color = Color.GREEN,
                        fg_color = Color.BRIGHT_RED,
                    ),
                ],
                [
                    RowFragment(
                        text = "CCCC",
                        bg_color = Color.BLUE,
                        fg_color = Color.BRIGHT_GREEN,
                    ),
                ],
                [
                    RowFragment(
                        text = "D",
                        bg_color = Color.BLUE,
                        fg_color = Color.BRIGHT_GREEN,
                    ),
                    RowFragment(
                        text = "D",
                        bg_color = Color.BLUE,
                        fg_color = Color.BRIGHT_CYAN,
                    ),
                    RowFragment(
                        text = "D",
                        bg_color = Color.BLUE,
                        fg_color = Color.BRIGHT_RED,
                    ),
                    RowFragment(
                        text = "D",
                        bg_color = Color.BLUE,
                        fg_color = Color.BRIGHT_MAGENTA,
                    ),
                ],
            ],
            [
                [
                    RowFragment(
                        text = "AA",
                        bg_color = Color.BLUE,
                        fg_color = Color.BRIGHT_GREEN,
                    ),
                    RowFragment(
                        text = "AA",
                        bg_color = Color.GREEN,
                        fg_color = Color.BRIGHT_CYAN,
                    ),
                ],
                [
                    RowFragment(
                        text = "BB",
                        bg_color = Color.BLUE,
                        fg_color = Color.BRIGHT_GREEN,
                    ),
                    RowFragment(
                        text = "B",
                        bg_color = Color.GREEN,
                        fg_color = Color.BRIGHT_CYAN,
                    ),
                    RowFragment(
                        text = "B",
                        bg_color = Color.GREEN,
                        fg_color = Color.BRIGHT_RED,
                    ),
                ],
                [
                    RowFragment(
                        text = "CCCC",
                        bg_color = Color.BLUE,
                        fg_color = Color.BRIGHT_GREEN,
                    )
                ],
                [
                    RowFragment(
                        text = "D",
                        bg_color = Color.BLUE,
                        fg_color = Color.BRIGHT_GREEN,
                    ),
                    RowFragment(
                        text = "D",
                        bg_color = Color.BLUE,
                        fg_color = Color.BRIGHT_CYAN,
                    ),
                    RowFragment(
                        text = "D",
                        bg_color = Color.BLUE,
                        fg_color = Color.BRIGHT_RED,
                    ),
                    RowFragment(
                        text = "D",
                        bg_color = Color.BLUE,
                        fg_color = Color.BRIGHT_MAGENTA,
                    ),
                ],
            ],
        ],
    )
    assert body.to_string(True) == text_reference

def test_body_from_text_correct_fullcolor():
    header = Header(
        width = 4,
        height = 4,
        delay = 200,
        loop_enable = True,
        color_mod = ColorMod.full,
        utf8 = False,
        datacols = 3,
        preview = DEFAULT_PREVIEW,
        audio = None,
        title = None,
        author = None,
    )
    body_reference = Body(
        frames = [
            [
                [
                    RowFragment(
                        text = "AA",
                        bg_color = Color.BLUE,
                        fg_color = Color.BRIGHT_GREEN,
                    ),
                    RowFragment(
                        text = "AA",
                        bg_color = Color.GREEN,
                        fg_color = Color.BRIGHT_CYAN,
                    ),
                ],
                [
                    RowFragment(
                        text = "BB",
                        bg_color = Color.BLUE,
                        fg_color = Color.BRIGHT_GREEN,
                    ),
                    RowFragment(
                        text = "B",
                        bg_color = Color.GREEN,
                        fg_color = Color.BRIGHT_CYAN,
                    ),
                    RowFragment(
                        text = "B",
                        bg_color = Color.GREEN,
                        fg_color = Color.BRIGHT_RED,
                    ),
                ],
                [
                    RowFragment(
                        text = "CCCC",
                        bg_color = Color.BLUE,
                        fg_color = Color.BRIGHT_GREEN,
                    ),
                ],
                [
                    RowFragment(
                        text = "D",
                        bg_color = Color.BLUE,
                        fg_color = Color.BRIGHT_GREEN,
                    ),
                    RowFragment(
                        text = "D",
                        bg_color = Color.BLUE,
                        fg_color = Color.BRIGHT_CYAN,
                    ),
                    RowFragment(
                        text = "D",
                        bg_color = Color.BLUE,
                        fg_color = Color.BRIGHT_RED,
                    ),
                    RowFragment(
                        text = "D",
                        bg_color = Color.BLUE,
                        fg_color = Color.BRIGHT_MAGENTA,
                    ),
                ],
            ],
            [
                [
                    RowFragment(
                        text = "AA",
                        bg_color = Color.BLUE,
                        fg_color = Color.BRIGHT_GREEN,
                    ),
                    RowFragment(
                        text = "AA",
                        bg_color = Color.GREEN,
                        fg_color = Color.BRIGHT_CYAN,
                    ),
                ],
                [
                    RowFragment(
                        text = "BB",
                        bg_color = Color.BLUE,
                        fg_color = Color.BRIGHT_GREEN,
                    ),
                    RowFragment(
                        text = "B",
                        bg_color = Color.GREEN,
                        fg_color = Color.BRIGHT_CYAN,
                    ),
                    RowFragment(
                        text = "B",
                        bg_color = Color.GREEN,
                        fg_color = Color.BRIGHT_RED,
                    ),
                ],
                [
                    RowFragment(
                        text = "CCCC",
                        bg_color = Color.BLUE,
                        fg_color = Color.BRIGHT_GREEN,
                    )
                ],
                [
                    RowFragment(
                        text = "D",
                        bg_color = Color.BLUE,
                        fg_color = Color.BRIGHT_GREEN,
                    ),
                    RowFragment(
                        text = "D",
                        bg_color = Color.BLUE,
                        fg_color = Color.BRIGHT_CYAN,
                    ),
                    RowFragment(
                        text = "D",
                        bg_color = Color.BLUE,
                        fg_color = Color.BRIGHT_RED,
                    ),
                    RowFragment(
                        text = "D",
                        bg_color = Color.BLUE,
                        fg_color = Color.BRIGHT_MAGENTA,
                    ),
                ],
            ],
        ],
    )
    text = "AAAAaabb1122\nBBBBaabc1122\nCCCCaaaa1111\nDDDDabcd1111\n\nAAAAaabb1122\nBBBBaabc1122\nCCCCaaaa1111\nDDDDabcd1111\n"
    assert body_reference.to_string(True) == Body.from_string(text, header).to_string(True)
