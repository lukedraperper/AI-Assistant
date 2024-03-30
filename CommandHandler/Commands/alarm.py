from datetime import datetime

def Alarm(num1, num2, amorpm, type):
    global StartUp
    if amorpm == "p.m.":
        amorpm = "PM."
    else:
        amorpm = "AM."
    # CS(f"Alarm set for {num1}:{num2} {amorpm}")
    num1 = int(num1)
    num2 = int(num2)
    if amorpm == "PM.":
        num1 += 12
    elif num1 == 12 and amorpm == "AM.":
        num1 -= 12
    while True:
        if num1 == datetime.now().hour and num2 == datetime.now().minute:
            break
    if type == "bed":
        StartUp()
    elif type == "Normal":
        # Play("alarm")
        pass