import os


def run_wait(command):
    r = os.popen(command)
    text = r.read()
    r.close()
    return text


pixel_color = run_wait("dd if=screen.dump bs=4 count=1 skip=1896719 2>null | xxd -ps")
print(pixel_color)
pixel_color = pixel_color[0:6]
print(pixel_color)
