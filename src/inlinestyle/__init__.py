from BeautifulSoup import BeautifulSoup as Soup
from soupselect import select
import cssutils
import re

class InlineStyler(object):
    def __init__(self, html_string):
        self._original_html = html_string
        self._soup = Soup(self._original_html)
    
    def _strip_styles(self):
        style_blocks = self._soup.findAll('style')
        css_list = []
        for style_block in style_blocks:
            if style_block.contents:
                css_list.append(style_block.contents[0])
            style_block.extract()
        return css_list
    
    def _load_sheet(self, css_list):
        parser = cssutils.CSSParser()
        self._sheet = parser.parseString(''.join(css_list))
        return self._sheet
    
    def _apply_rules(self):
        for item in self._sheet.cssRules:
            if item.type == item.STYLE_RULE:
                selector = item.selectorText
                items = select(self._soup, selector)
                for element in items:
                    styles = item.style.cssText.splitlines()
                    new_styles = [style.replace(';','') for style in styles]
                    current_styles = element.get('style','').split(';')
                    current_styles.extend(new_styles)
                    current_styles = filter(None, current_styles)
                    element['style'] = ';'.join(current_styles)
        return self._soup
    
    def convert(self):
        css_list = self._strip_styles()
        self._load_sheet(css_list)
        html = self._apply_rules()
        return str(html)

def remove_whitepace(input_string):
    import string
    filtered_string = filter(lambda x: x not in string.whitespace, input_string)
    return filtered_string
