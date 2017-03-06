# -*- coding: utf-8 -*-

import os
import flask_recipes
import unittest
import tempfile

class FlaskRecipesTestCase(unittest.TestCase):
    
    def setUp(self):
        self.db_fd, flask_recipes.app.config['DATABASE'] = tempfile.mkstemp()
        flask_recipes.app.config['TESTING'] = True
        self.app = flask_recipes.app.test_client()
        with flask_recipes.app.app_context():
            flask_recipes.init_db()
            
    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flask_recipes.app.config['DATABASE'])
        
    def login(self, username, password):
        return self.app.post('/login', data=dict(
                username = username,
                password = password), follow_redirects=True)
        
    def logout(self):
        return self.app.get('/logout', follow_redirects=True)
        
    def test_inital_welcome_page(self):
        rv = self.app.get('/')
        assert b'Welcome! Please Log In To View Recipes!' in rv.data
    
    def test_login_logout(self):
        rv = self.login('admin', '0000')
        assert b'Log In Successful' in rv.data
        rv = self.login('adminn', '0000')
        assert b'Invalid Username/Password' in rv.data
        rv = self.login('admin', '0001')
        assert b'Invalid Username/Password' in rv.data
    
    def test_empty_db(self):
        rv = self.login('admin', '0000')
        assert b'Unbelievable.  No entries here so far' in rv.data
        
    def test_flash_messages(self):
        self.login('admin', '0000')
        rv = self.app.post('/addrecipe', data=dict(
            recipe_name = 'Grilled Cheese',
            recipe_description = "It's Grilled Cheese yo!"),follow_redirects = True)
        assert b'Unvelievable. No entries here so far' not in rv.data
        assert b'Grilled Cheese' in rv.data
        assert b"It's Grilled Cheese yo!" in rv.data
        
        
if __name__ == '__main__':
    unittest.main()
    
    

    
    
    
    
    