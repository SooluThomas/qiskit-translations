from qiskit.circuit import QuantumCircuit
from qiskit.circuit.library import PhaseEstimation
import qiskit.tools.jupyter
unitary = QuantumCircuit(2)
unitary.x(0)
unitary.y(1)
circuit = PhaseEstimation(3, unitary)
%circuit_library_info circuit