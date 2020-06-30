from qiskit.circuit.library import HiddenLinearFunction
import qiskit.tools.jupyter
A = [[1, 1, 0], [1, 0, 1], [0, 1, 1]]
circuit = HiddenLinearFunction(A)
%circuit_library_info circuit