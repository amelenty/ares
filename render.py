import tcod

OFFSET_X = 5
OFFSET_Y = 0


def render_all(console, entities, game_map, fov_map, fov_recompute, screen_width, screen_height, colors):
    if fov_recompute:
        for y in range(game_map.height):
            for x in range(game_map.width):
                visible = tcod.map_is_in_fov(fov_map, x, y)
                wall = game_map.tiles[x][y].block_sight

                ox = OFFSET_X + x
                oy = OFFSET_Y + y

                if visible:
                    if wall:
                        tcod.console_set_char_background(console, ox, oy, colors.get('light_wall'), tcod.BKGND_SET)
                    else:
                        tcod.console_set_char_background(console, ox, oy, colors.get('light_ground'), tcod.BKGND_SET)
                    game_map.tiles[x][y].explored = True
                elif game_map.tiles[x][y].explored:
                    if wall:
                        tcod.console_set_char_background(console, ox, oy, colors.get('dark_wall'), tcod.BKGND_SET)
                    else:
                        tcod.console_set_char_background(console, ox, oy, colors.get('dark_ground'), tcod.BKGND_SET)

    # Draw all entities in the list
    for entity in entities:
        draw_entity(console, entity, fov_map)

    tcod.console_blit(console, 0, 0, screen_width, screen_height, 0, 0, 0)


def clear_all(console, entities):
    for entity in entities:
        clear_entity(console, entity)


def draw_entity(console, entity, fov_map):
    if fov_map.fov[entity.y][entity.x]:
        tcod.console_set_default_foreground(console, entity.color)
        tcod.console_put_char(console, OFFSET_X + entity.x, OFFSET_Y + entity.y, entity.char, tcod.BKGND_NONE)


def clear_entity(console, entity):
    # erase the character that represents this object
    tcod.console_put_char(console, OFFSET_X + entity.x, OFFSET_Y + entity.y, ' ', tcod.BKGND_NONE)
