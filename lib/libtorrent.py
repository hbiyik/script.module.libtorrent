import abi
import sys


__m = abi.load("script.module.libtorrent", "libtorrent")
import sys
sys.modules[__name__] = __m
