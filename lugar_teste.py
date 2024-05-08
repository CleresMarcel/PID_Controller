# Brincando com o PID


import numpy as np

import matplotlib.pyplot as plt
import control as ctrl

Kp = 800.0
Ki = 70.0
Kaw = 1.0
Kd = 20.0
T_C = 1.0

num = [Kd, Kp, Ki]
den = [1, 2,3,4]
test = ctrl.TransferFunction(num, den)
plt.figure()
ctrl.root_locus(test)
plt.title('Root Locus Plot of PID Controller')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.grid(True)
plt.show()