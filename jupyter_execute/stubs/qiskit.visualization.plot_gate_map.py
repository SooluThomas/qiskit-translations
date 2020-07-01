from qiskit.test.ibmq_mock import mock_get_backend
mock_get_backend('FakeVigo')

from qiskit import QuantumCircuit, execute, IBMQ
from qiskit.visualization import plot_gate_map
%matplotlib inline

provider = IBMQ.load_account()
accountProvider = IBMQ.get_provider(hub='ibm-q')
backend = accountProvider.get_backend('ibmq_vigo')
plot_gate_map(backend)