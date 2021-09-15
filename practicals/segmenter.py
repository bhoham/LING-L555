####splits a text corpus into sentences

import sys
rawtext = sys.stdin.read()
segmentedtext = rawtext.replace(". ",".\n")
