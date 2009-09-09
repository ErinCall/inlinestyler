from inlinestyle import InlineStyler
class TestCase(object):
    def setup(self):
        f = open('tests/test.html','r')
        self.html = f.read()
        f.close()
    
    def test_style_striping(self):
        styler = InlineStyler(self.html)
        css_list = styler._strip_styles()
        #css_list is a certain length
        assert len(css_list) == 4
        
    