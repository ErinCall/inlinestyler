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

    '''
    def test_style_application(self):
        assert False, 'not yet implemented'

    def test_conversion(self):
        assert False, 'not yet implemented'
    '''

    def test_remove_whitepace(self):
        inpt = 'body{\r\ntest}\t '
        string2 = remove_whitepace(inpt)
        eq_(string2, 'body{test}')

    '''
    def test_css_load(self):
        styler = InlineStyler(self.html)
        css_list = styler._strip_styles()
        string = ''.join(css_list)
        assert False, 'not yet implemented'
    '''


class TestConversion(TestCase):
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
    <div class="div" style="font-weight: bold;font-family: 'Courier New';background: #fff;color: #000">
        div text
    </div>
<div style="font-weight: bold;font-family: 'Courier New'">
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

    def test_handles_multiple_classes(self):
        html = """
            <style>
                div.class1.class2 {
                    color: red;
                }
            </style>
            <div class="class1 class2">stuff</div>
        """
        styler = InlineStyler(html)
        new_html = styler.convert()
        eq_(new_html.strip(), '<div class="class1 class2" style="color: red">stuff</div>')

    def test_handles_comma_separated_classes(self):
        html = u"""
            <style>
                .noise-class, .target {
                    background-color: #FF00FF
                }
            </style>
            <div class="target">
            </div>
        """
        expected_html = u"""

<div class="target" style="background-color: #F0F">
</div>
"""
        styler = InlineStyler(html)
        new_html = styler.convert()
        eq_(expected_html, new_html)

    def test_remove_class_attribute(self):
        styler = InlineStyler('<style></style><div class="test">test</div>')
        new_html = styler.convert(remove_class=True)
        eq_(new_html, '<div>test</div>')

    def test_remove_id_attribute(self):
        styler = InlineStyler('<style></style><div id="test">test</div>')
        new_html = styler.convert(remove_id=True)
        eq_(new_html, '<div>test</div>')
