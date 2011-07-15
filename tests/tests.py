from inlinestyle.styler import InlineStyler, remove_whitespace
class TestCase(object):
    def setup(self):
        f = open('tests/test.html','r')
        self.html = f.read()
        f.close()
        f = open('tests/expected.html','r')
        self.expected = f.read()
        f.close()

    def test_external_load(self):
        styler = InlineStyler("<link type="text/css" href='test_type.css' ><div>test</div>", host="example.com",relative_url="/styles/")
        tags = self._soup.findAll({'link':True,'style':True})

        assert False

    def test_strip_styles(self):
        styler = InlineStyler(self.html)
        css_list = styler._strip_styles()
        #css_list is a certain length
        assert len(css_list) == 4

    def test_remove_whitepace(self):
        inpt = 'body{\r\ntest}\t '
        string2 = remove_whitespace(inpt)
        print string2
        assert string2 == 'body{test}'

    def test_css_load(self):
        styler = InlineStyler(self.html)
        css_list = styler._strip_styles()
        print css_list
        string = ''.join(css_list)
        
    def test_convert(self):
        styler = InlineStyler(self.html)
        new_html = styler.convert()
        #print new_html
        #print self.expected
        import difflib

        diff = difflib.unified_diff(new_html, self.expected)
        print ''.join(list(diff))
        assert new_html
        assert new_html == self.expected
