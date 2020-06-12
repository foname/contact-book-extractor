import unittest
from song_decoder import songDecoder

class TestSongDecoder(unittest.TestCase):
    def test_basic_string(self):
        self.assertEqual(songDecoder("WUBWEWUBAREWUBWUBTHEWUBBACKYARDWUBMYWUBFRIENDWUB"), "WE ARE THE BACKYARD MY FRIEND", "Should match given example")
    
    def test_replace_one_space(self):
        self.assertEqual(songDecoder("AWUBBWUBC"), "A B C", "WUB should be replaced by 1 space")
        
    def test_result_multiple_one_space(self):
        self.assertEqual(songDecoder("AWUBWUBWUBBWUBWUBWUBC"), "A B C", "multiples WUB should be replaced by only 1 space")
    
    def test_trim_whitespace(self):
        self.assertEqual(songDecoder("WUBAWUBBWUBCWUB"), "A B C","heading or trailing spaces should be removed")


if __name__ == '__main__':
    unittest.main()