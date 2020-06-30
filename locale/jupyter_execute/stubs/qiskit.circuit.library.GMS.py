from qiskit.circuit.library import GMS
import qiskit.tools.jupyter
import numpy as np
circuit = GMS(num_qubits=3, theta=[[0, np.pi/4, np.pi/8],
                                   [0, 0, np.pi/2],
                                   [0, 0, 0]])
%circuit_library_info circuit.decompose()