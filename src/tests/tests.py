from inlinestyle import InlineStyler, remove_whitepace
import os.path
from nose.tools import eq_

class TestCase(object):
    def setup(self):
        test_path = os.path.dirname(__file__)
        test_html_file = os.path.join(test_path, 'test.html')
        f = open(test_html_file,'r')
        self.html = f.read()
        f.close()

    def test_strip_styles(self):
        styler = InlineStyler(self.html)
        css_list = styler._strip_styles()
        eq_(len(css_list), 4)

    def test_style_application(self):
        assert False, 'not yet implemented'

    def test_conversion(self):
        assert False, 'not yet implemented'

    def test_remove_whitepace(self):
        inpt = 'body{\r\ntest}\t '
        string2 = remove_whitepace(inpt)
        eq_(string2, 'body{test}')

    def test_css_load(self):
        styler = InlineStyler(self.html)
        css_list = styler._strip_styles()
        string = ''.join(css_list)
        assert False, 'not yet implemented'


class Conversion(TestCase):
    def test_integration(self):
        styler = InlineStyler(self.html)
        new_html = styler.convert()
        eq_(new_html, """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>untitled</title>


</head>

<body class="body" style="background: #000;color: #FFF;font-size: 10px">
    Body text
    <div class="div" style="font-weight: bold;background: #fff;color: #000">
        div text
    </div>
<div style="font-weight: bold">
        empty div
    </div>

<p class="p" style="background: #fff;color: #000">
        p text
    </p>
</body>
</html>
""")

    def test_handles_documents_with_an_empty_style_tag(self):
        styler = InlineStyler('<style></style>')
        new_html = styler.convert()
        eq_(new_html, '')
