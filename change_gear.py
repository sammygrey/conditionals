def change_gear(str_gear):
    print("Gear changed to", str_gear)
    print("displayed gear:", str_gear)

def process_speed(speed):
    if 0 <= speed < 30:
        change_gear('1')
        return
    elif speed < 50:
        change_gear('2')
        return
    elif speed < 90:
        change_gear('3')
        return
    elif 90 <= speed:
        change_gear('4')
        return
    else:
        change_gear('R')

if __name__ == "__main__":
    process_speed(40)