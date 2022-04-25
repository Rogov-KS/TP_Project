def update(fortress_group, timer):
    # for fort in fortress_group:
    #     fort.update()

    if(timer & 10 == 0):
        fortress_group.update()

    return
