from qiskit.quantum_info import Statevector

psi = Statevector.from_label('-0')
print(psi.to_dict())

import numpy as np
from qiskit.quantum_info import Statevector

vec = np.zeros(9)
vec[0] = 1 / np.sqrt(2)
vec[-1] = 1 / np.sqrt(2)
psi = Statevector(vec, dims=(3, 3))
print(psi.to_dict())

import numpy as np
from qiskit.quantum_info import Statevector

vec = np.zeros(2 * 10)
vec[0] = 1 / np.sqrt(2)
vec[-1] = 1 / np.sqrt(2)
psi = Statevector(vec, dims=(2, 10))
print(psi.to_dict())