from qiskit import pulse
from qiskit.test.mock import FakeOpenPulse2Q

backend = FakeOpenPulse2Q()
with pulse.build(backend):
    assert pulse.control_channels(0, 1) == [pulse.ControlChannel(0)]