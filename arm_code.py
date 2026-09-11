while True:
    select = False
    if "ch".is_clicked():
        select = True
    number_selected = -1
    thumb_speed_mode = 3
    pointer_speed_mode = 3
    middle_speed_mode = 3
    ring_speed_mode = 3
    pinky_speed_mode = 3
    selected = None
    while select:
        if "1".is_pressed():
            selected = 1
        elif "2".is_pressed():
            selected = 2
        elif "3".is_pressed():
            selected = 3
        elif "4".is_pressed():
            selected = 4
        elif "5".is_pressed():
            selected = 5
        while selected == 1:
            if "ch+".is_clicked():
                if thumb_speed_mode < 5:
                    thumb_speed_mode += 1
                    selected = -1
                    select = False
            elif "ch-".is_clicked():
                if thumb_speed_mode > 1:
                    thumb_speed_mode -= 1
                    selected = -1
                    select = False
        while selected == 2:
            if "ch+".is_clicked():
                if pointer_speed_mode < 5:
                    thumb_speed_mode += 1
                    selected = -1
                    select = False
            elif "ch-".is_clicked():
                if pointer_speed_mode > 1:
                    pointer_speed_mode -= 1
                    selected = -1
                    select = False  
        while selected == 3:
            if "ch+".is_clicked():
                if pointer_speed_mode < 5:
                    pointer_speed_mode += 1
                    selected = -1
                    select = False
            elif "ch-".is_clicked():
                if pointer_speed_mode > 1:
                    pointer_speed_mode -= 1  
                    selected = -1
                    select = False
        while selected == 4:
            if "ch+".is_clicked():
                if middle_speed_mode < 5:
                    middle_speed_mode += 1
                    selected = -1
                    select = False
            elif "ch-".is_clicked():
                if middle_speed_mode > 1:
                    middle_speed_mode -= 1
                    selected = -1
                    select = False
        while selected == 5:
            if "ch+".is_clicked():
                if ring_speed_mode < 5:
                    ring_speed_mode += 1
                    selected = -1
                    select = False
            elif "ch-".is_clicked():
                if ring_speed_mode > 1:
                    ring_speed_mode -= 1
                    selected = -1
                    select = False
