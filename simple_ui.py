import os
def baseui(color, name, number):
    os.system("cls")
    os.system(f"color {color}")
    
    print("-" * number)

    srt_out = str(input(f"{name}:"))

    os.system("color 7")
    
    return srt_out


