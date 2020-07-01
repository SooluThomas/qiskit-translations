from qiskit.circuit.library import FourierChecking
import qiskit.tools.jupyter
f = [1, -1, -1, -1]
g = [1, 1, -1, -1]
circuit = FourierChecking(f, g)
%circuit_library_info circuit