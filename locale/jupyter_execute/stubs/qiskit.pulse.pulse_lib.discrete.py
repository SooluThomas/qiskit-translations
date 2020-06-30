import matplotlib.pyplot as plt
from qiskit.pulse.pulse_lib import sawtooth
import numpy as np

duration = 100
amp = 1
period = duration
sawtooth_wave = np.real(sawtooth(duration, amp, period).samples)
plt.plot(range(duration), sawtooth_wave)

import matplotlib.pyplot as plt
from qiskit.pulse.pulse_lib import triangle
import numpy as np

duration = 100
amp = 1
period = duration
triangle_wave = np.real(triangle(duration, amp, period).samples)
plt.plot(range(duration), triangle_wave)