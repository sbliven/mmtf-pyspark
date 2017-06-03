#!/usr/bin/env python
#!/usr/bin/env python
'''
Demo0b.py: Example reading a list of PDB IDs from a local MMTF Hadoop sequence \
file into a tubleRDD.

Authorship information:
__author__ = "Peter Rose"
__maintainer__ = "Mars Huang"
__email__ = "marshuang80@gmai.com:
__status__ = "Warning"
'''
# TODO Traceback "ResourceWarning: unclosed file"

import unittest
from pyspark import SparkConf, SparkContext
from ..MmtfReader import readSequenceFile

path = 'full'
stringIds = "1AQ1,1B38,1B39,1BUH,1C25,1CKP,1DI8,1DM2,1E1V,1E1X,1E9H,1F5Q,1FIN,1FPZ,1FQ1,1FQV,1FS1"
pdbIds = stringIds.split(',')

class testReadSequenceFile(unittest.TestCase):

    def test_size(self):
        self.assertEqual(len(pdbIds),pdb.count())

if __name__ == '__main__':
    conf = SparkConf().setMaster("local[*]").setAppName('Demo0b')
    sc = SparkContext(conf=conf)
    pdb = readSequenceFile(path, sc, pdbId = pdbIds)
    unittest.main()
    sc.close()