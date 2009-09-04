from BeautifulSoup import BeautifulSoup as Soup
from soupselect import select
import cssutils

class InlineStyler(object):
    def __init__(self, html_string):
        self._original_html = html_string
        self._soup = Soup(self._original_html)
    
    def _strip_styles(self):
        style_blocks = self._soup.findAll('style')
        css_list = []
        for style_block in style_blocks:
            style_innards.append(style_block.contents[0])
            style_block.extract()
        return css_list
    
    def _load_sheet(self, css_list):
        parser = cssutils.CSSParser()
        self._sheet = parser.parseString(''.join(css_list))
    
    def _apply_rules(self):
        for item in self._sheet.cssRules:
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

def do_work(html):
    """
    temporary function
    """
    print html
    soup_doc, style_innards = strip_style_information(html)
    sheet = parse_css(style_innards)
    s = apply_rules(soup_doc, sheet)
    print str(s)
