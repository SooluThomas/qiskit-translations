from qiskit.circuit.library import OR
import qiskit.tools.jupyter
circuit = OR(5)
%circuit_library_info circuit

from qiskit.circuit.library import OR
import qiskit.tools.jupyter
circuit = OR(5, flags=[-1, 0, 0, 1, 1])
%circuit_library_info circuit