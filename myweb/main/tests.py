from django.test import TestCase

import unittest
import views
from main.forms import InputName

class viewsTesting(unittest.TestCase):

        #tests that return is not none.
        def test_graphVisual(self):
            result = views.graph_visual()
            self.assertIsNotNone()

        #tests that return is not none.
        def test_pieVisual(self):
            result = views.pie_visual()
            self.assertIsNotNone()

        #tests that return is not none.
        def test_graphVisual(self):
            result = views.graph_visual()
            self.assertIsNotNone()

        #tests to see if remove_links returns true
        def test_removeLinks(self):
            result = views.remove_links()
            self.assertTrue()

        def test_removeLinks(self):
            sample_tweet = tweet('This is a link: @www.harrisonblack.com/rewards')

            self.assertEqual(sample.remove_links, 'This is a link: ')    

if __name__ == '__main__':
    unittest.main()
