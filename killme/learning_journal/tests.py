import unittest

from pyramid import testing


def test_detail_view_has_title():
    from .views import detail_view

    request = testing.DummyRequest()
    info = detail_view(request)
    assert 'title' in info.keys()

# @pytest.fixture()
# def testapp():
#     from learning_journal import main
#     app = main({})
#     from webtest import TestApp
#     import TestApp(app)
    

class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_my_view(self):
        from .views import my_view
        request = testing.DummyRequest()
        info = my_view(request)
        self.assertEqual(info['project'], 'learning_journal')


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from learning_journal import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_root(self):
        res = self.testapp.get('/', status=200)
        self.assertTrue(b'Pyramid' in res.body)
