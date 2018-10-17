import tcod

from entity import Entity
from input_handlers import handle_keys
from render import render_all, clear_all
from world.game_map import GameMap


def main():
    screen_width = 80
    screen_height = 50
    map_width = 70
    map_height = 45

    colors = {
        'dark_wall': tcod.darkest_gray,
        'dark_ground': tcod.darker_gray
    }

    player = Entity(map_width // 2, map_height // 2, '@', tcod.green)
    npc = Entity(map_width // 2 - 5, map_height // 2, 'N', tcod.darker_green)
    entities = [npc, player]

    tcod.console_set_custom_font('arial10x10.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)

    console = tcod.console_init_root(screen_width, screen_height, 'tcod tutorial revised', False)

    game_map = GameMap(map_width, map_height)

    key = tcod.Key()
    mouse = tcod.Mouse()

    while not tcod.console_is_window_closed():
        tcod.sys_check_for_event(tcod.EVENT_KEY_PRESS, key, mouse)

        render_all(console, entities, game_map, screen_width, screen_height, colors)

        tcod.console_flush()

        clear_all(console, entities)

        action = handle_keys(key)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            if not game_map.is_blocked(player.x + dx, player.y + dy):
                player.move(dx, dy)

        if exit:
            return True

        if fullscreen:
            tcod.console_set_fullscreen(not tcod.console_is_fullscreen())


if __name__ == '__main__':
    main()
