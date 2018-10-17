import tcod

from handle_keys import handle_keys


def main():
    screen_width = 80
    screen_height = 50

    player_x = screen_width // 2
    player_y = screen_height // 2

    tcod.console_set_custom_font('arial10x10.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)

    console = tcod.console_init_root(screen_width, screen_height, 'tcod tutorial revised', False)

    key = tcod.Key()
    mouse = tcod.Mouse()

    while not tcod.console_is_window_closed():
        tcod.sys_check_for_event(tcod.EVENT_KEY_PRESS, key, mouse)

        tcod.console_set_default_foreground(console, tcod.white)
        tcod.console_put_char(console, player_x, player_y, '@', tcod.BKGND_NONE)
        tcod.console_flush()

        action = handle_keys(key)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            tcod.console_put_char(console, player_x, player_y, ' ', tcod.BKGND_NONE)
            dx, dy = move
            player_x += dx
            player_y += dy

        if exit:
            return True

        if fullscreen:
            tcod.console_set_fullscreen(not tcod.console_is_fullscreen())


if __name__ == '__main__':
    main()
