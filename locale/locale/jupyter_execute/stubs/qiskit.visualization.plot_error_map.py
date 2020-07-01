from qiskit.test.ibmq_mock import mock_get_backend
mock_get_backend('FakeVigo')

from qiskit import QuantumCircuit, execute, IBMQ
from qiskit.visualization import plot_error_map
%matplotlib inline

IBMQ.load_account()
provider = IBMQ.get_provider(hub='ibm-q')
backend = provider.get_backend('ibmq_vigo')
plot_error_map(backend)