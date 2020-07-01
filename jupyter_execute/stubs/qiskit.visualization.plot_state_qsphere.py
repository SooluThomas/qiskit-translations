from qiskit import QuantumCircuit, BasicAer, execute
from qiskit.visualization import plot_state_qsphere
%matplotlib inline

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

backend = BasicAer.get_backend('statevector_simulator')
job = execute(qc, backend).result()
plot_state_qsphere(job.get_statevector(qc))