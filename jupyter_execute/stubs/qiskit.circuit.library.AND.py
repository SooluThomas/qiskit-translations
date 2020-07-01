from qiskit.circuit.library import AND
import qiskit.tools.jupyter
circuit = AND(5)
%circuit_library_info circuit

from qiskit.circuit.library import AND
import qiskit.tools.jupyter
circuit = AND(5, flags=[-1, 0, 0, 1, 1])
%circuit_library_info circuit