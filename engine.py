import tcod


def main():
    screen_width = 80
    screen_height = 50

    player_x = screen_width // 2
    player_y = screen_height // 2

    tcod.console_set_custom_font('arial10x10.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)

    console = tcod.console_init_root(screen_width, screen_height, 'libtcod tutorial revised', False)

    while not tcod.console_is_window_closed():
        tcod.console_set_default_foreground(console, tcod.white)
        tcod.console_put_char(console, player_x, player_y, '@', tcod.BKGND_NONE)
        tcod.console_flush()

        key = tcod.console_check_for_keypress()

        if key.vk == tcod.KEY_UP:
            tcod.console_put_char(console, player_x, player_y, ' ', tcod.BKGND_NONE)
            player_y -= 1
        elif key.vk == tcod.KEY_DOWN:
            tcod.console_put_char(console, player_x, player_y, ' ', tcod.BKGND_NONE)
            player_y += 1
        elif key.vk == tcod.KEY_LEFT:
            tcod.console_put_char(console, player_x, player_y, ' ', tcod.BKGND_NONE)
            player_x -= 1
        elif key.vk == tcod.KEY_RIGHT:
            tcod.console_put_char(console, player_x, player_y, ' ', tcod.BKGND_NONE)
            player_x += 1
        elif key.vk == tcod.KEY_ESCAPE:
            return True


if __name__ == '__main__':
    main()
