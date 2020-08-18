from qiskit import pulse
from qiskit.test.mock import FakeOpenPulse2Q

backend = FakeOpenPulse2Q()

transpiler_settings = {'optimization_level': 3}

with pulse.build(backend,
                 default_transpiler_settings=transpiler_settings):
    print(pulse.active_transpiler_settings())