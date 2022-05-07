import configuration as config


def update(fortress_group, army_group, cursor_group, timer):
    if timer > config.program_time * 1000 / config.updates_in_second:
        config.program_time += 1
        fortress_group.update()
    army_group.update(army_group)  # пофиксить, чтобы добиться скорости в секунду, незавясящей от FPS
    cursor_group.update()
    return
