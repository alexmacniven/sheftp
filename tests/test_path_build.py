import os
import tempfile
import unittest

from sheftp.com.shell import path_build

class TestPathBuild(unittest.TestCase):

    def setUp(self):
        # Create a temp directory and cd
        self.currentdir = tempfile.TemporaryDirectory()
        os.chdir(self.currentdir.name)

    def test_when_source_file_supplied(self):
        """Test when a source file name only is supplied"""   
        src = 'README.md'
        source, destin = path_build(src)
        self.assertEqual(source, src)
        self.assertEqual(destin, os.path.join(self.currentdir.name, src))

    def test_when_destin_dir_supplied(self):
        """Test when a destination directory is supplied"""
        src = 'README.md'
        dst = '/usr/etc/'
        source, destin = path_build(src, dst)
        self.assertEqual(source, src)
        self.assertEqual(destin, os.path.join(dst, src))

    def test_when_destin_path_supplied(self):
        """test when a destination path is supplied"""
        src = 'README.md'
        dst = '/usr/etc/README'
        source, destin = path_build(src, dst)
        self.assertEqual(source, src)
        self.assertEqual(destin, dst)

    # def tearDown(self):
    #     self.currentdir.cleanup()


if __name__ == '__main__':
    unittest.main()
