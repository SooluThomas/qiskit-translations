from qiskit import pulse

with pulse.build() as pulse_prog:
    pulse.snapshot('first', 'statevector')