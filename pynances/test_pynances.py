"""
Miscellaneous tests for Pynances.
"""
import unittest
from datetime import date

from flask.ext.testing import TestCase

from .pynances import app
from .pynances import Currency
from .pynances import db
from .pynances import Expense
from .pynances import Tag


class FlaskTestCaseBase(TestCase):
    """
    A base for the following test cases.
    """
    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        return app

    def setUp(self):
        self.client = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class PynancesConfigTestCase(FlaskTestCaseBase):
    """
    Tests for app.py's app.config attribute.
    """
    def test_DEBUG_is_defined(self):
        self.assertIn('DEBUG', app.config)

    def test_DEBUG_is_True(self):
        self.assertTrue(app.config['DEBUG'])

    def test_SQLALCHEMY_DATABASE_URI_is_defined(self):
        self.assertIn('SQLALCHEMY_DATABASE_URI', app.config)

    def test_SQLALCHEMY_DATABASE_URI_contains_sqlite(self):
        # For the time being!
        self.assertIn('sqlite', app.config['SQLALCHEMY_DATABASE_URI'])


class PynancesModelsTestCase(FlaskTestCaseBase):
    """
    Tests for app.py's models.
    """
    def test_a_Currency_can_be_created(self):
        currency = Currency(abbreviation='USD',
            description='United States Dollars')
        db.session.add(currency)
        db.session.commit()
        self.assertEqual(Currency.query.get(1), currency)

    def test_a_Tag_can_be_created(self):
        tag = Tag(value=u'new tag')
        db.session.add(tag)
        db.session.commit()
        self.assertEqual(Tag.query.get(1), tag)

    def test_an_Expense_without_Tags_can_be_created(self):
        currency = Currency(abbreviation='USD',
            description='United States Dollars')
        db.session.add(currency)
        db.session.commit()
        date_added = date.today()
        amt = 10.21
        expense = Expense(date=date_added, amt=amt,
            currency_id=currency.id)
        db.session.add(expense)
        db.session.commit()
        self.assertEqual(Expense.query.get(1), expense)

    def test_an_Expense_with_Tags_can_be_created(self):
        currency = Currency(abbreviation='USD',
            description='United States Dollars')
        db.session.add(currency)
        db.session.commit()
        date_added = date.today()
        amt = 10.21
        expense = Expense(date=date_added, amt=amt,
            currency_id=currency.id)
        db.session.add(expense)
        db.session.commit()
        self.assertEqual(Expense.query.get(1), expense)

        tag = Tag(value=u'new tag')
        expense.tags.append(tag)
        db.session.commit()
        self.assertEqual(Expense.query.get(1), expense)
        self.assertEqual(len(expense.tags), 1)


#class PynancesAPITestCase(FlaskTestCaseBase):
    #"""
    #Tests for the endpoints created in app.py with Flask-restless.
    #"""
    #def setUp(self):
        #super(FlaskTestCaseBase, self).setUp()
        #self.expense_endpoint = '/api/expense'
        #self.tag_endpoint = '/api/tag'

    #def test_Tag_endpoint_exists(self):
        #resp = self.client.get(self.tag_endpoint,
            #headers={'content-type': 'application/json'})
        #self.assertEqual(resp.status_code, 200)

    #def test_Tag_endpoint_allows_GET(self):
        ## returns 1 item after it has been added to the DB
        #raise NotImplementedError

    #def test_Tag_endpoint_allows_POST(self):
        #tag = {'value': u'new tag'}
        #resp = self.client.post(self.tag_endpoint, data=tag)
        #self.assertEqual(resp.status_code, 200)

    #def test_Tag_endpoint_allows_PUT(self):
        #raise NotImplementedError

    #def test_Tag_endpoint_allows_DELETE(self):
        #raise NotImplementedError

    #def test_Expense_endpoint_exists(self):
        #resp = self.client.get(self.expense_endpoint,
            #headers={'content-type': 'application/json'})
        #self.assertEqual(resp.status_code, 200)

    #def test_Expense_endpoint_allows_GET(self):
        ## returns 1 item after it has been added to the DB
        #raise NotImplementedError

    #def test_Expense_endpoint_allows_POST(self):
        #raise NotImplementedError

    #def test_Expense_endpoint_allows_PUT(self):
        #raise NotImplementedError

    #def test_Expense_endpoint_allows_DELETE(self):
        #raise NotImplementedError


class PynancesRoutesTestCase(FlaskTestCaseBase):
    """
    Tests for app.py's various routes.
    """
    def test_index_returns_200(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_about_returns_200(self):
        resp = self.client.get('/about')
        self.assertEqual(resp.status_code, 200)

    def test_undefined_route_returns_404(self):
        resp = self.client.get('/this-will-not-exist')
        self.assertEqual(resp.status_code, 404)


if __name__ == '__main__':
    unittest.main()

