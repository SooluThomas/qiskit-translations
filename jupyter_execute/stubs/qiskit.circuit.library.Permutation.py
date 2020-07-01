from qiskit.circuit.library import Permutation
import qiskit.tools.jupyter
A = [2,4,3,0,1]
circuit = Permutation(5, A)
circuit.draw('mpl')

from qiskit.circuit.library import Permutation
import qiskit.tools.jupyter
A = [2,4,3,0,1]
circuit = Permutation(5, A)
%circuit_library_info circuit.decompose()