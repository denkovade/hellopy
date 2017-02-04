import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import hello as h


def test_helloPV():
	a = h.hello()

	assert a == "Hello, PV!"
