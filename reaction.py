import numpy as np
import cv2
import time
import mss
import mouse

X_OFFSET = 500
Y_OFFSET = 500

sct = mss.mss()
mon = {"top": Y_OFFSET, "left": X_OFFSET, "width": 1, "height": 1}

while True:

    last_time = time.perf_counter()

    printscreen_np = np.asarray(sct.grab(mon))

    if printscreen_np[0][0][2] == 75:
        print(f"Screen grab {(time.perf_counter() - last_time) * 1000} ms")
        last_time = time.perf_counter()
        mouse.click()
        print(f"Click {(time.perf_counter() - last_time) * 1000} ms")

        time.sleep(1)
