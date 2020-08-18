from qiskit.circuit.library import MCMTVChain, ZGate
import qiskit.tools.jupyter
circuit = MCMTVChain(ZGate(), 2, 2)
%circuit_library_info circuit.decompose()