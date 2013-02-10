import unittest

import pynances


class PynancesFlaskAppTestCase(unittest.TestCase):
    """
    Tests for app.py's various routes.
    """
    def setUp(self):
        self.app = pynances.app.test_client()

    def tearDown(self):
        pass

    def test_index_returns_200(self):
        resp = self.app.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_missing_route_returns_404(self):
        resp = self.app.get('/this-will-not-exist')
        self.assertEqual(resp.status_code, 404)


if __name__ == '__main__':
    unittest.main()
