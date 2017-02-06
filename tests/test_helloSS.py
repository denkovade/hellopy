import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import helloSS as h


def test_helloSS():
	a = h.hello()

	assert a == "Hello, SS!"
