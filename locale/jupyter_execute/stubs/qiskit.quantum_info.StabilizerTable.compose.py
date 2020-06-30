from qiskit.quantum_info.operators import StabilizerTable

current = StabilizerTable.from_labels(['+I', '-X'])
other =  StabilizerTable.from_labels(['+X', '-Z'])
print(current.compose(other))