from qiskit.circuit.library import QFT
import qiskit.tools.jupyter
circuit = QFT(4)
%circuit_library_info circuit

from qiskit.circuit.library import QFT
import qiskit.tools.jupyter
circuit = QFT(4).inverse()
%circuit_library_info circuit

from qiskit.circuit.library import QFT
import qiskit.tools.jupyter
circuit = QFT(5, approximation_degree=2)
%circuit_library_info circuit