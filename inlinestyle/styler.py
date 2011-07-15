import cssutils
import requests
from BeautifulSoup import BeautifulSoup as Soup
from .soupselect import select

class InlineStyler(object):
    def __init__(self, html_string, host=None, relative_url=None):
        self._original_html = html_string
        self._soup = Soup(self._original_html)
        self.host = host
        self.relative_url = relative_url
    
    def _strip_styles(self):
        tags = self._soup.findAll({'link':True,'style':True})
        css_list = []
        for tag in tags:
            _style = self._load_style(tag)
            if _style:
                css_list.append(_style)
            tag.extract()
        return css_list

    def _load_external(self, tag):
        if tag.get('rel') != 'stylesheet' and tag.get('type') != 'stylesheet':
            return
        url = tag.get('href')
        if url.startswith('http://') or url.startswith('https://'):
            pass
        elif url.startswith('/'):
            if self.host:
                url = self.host + url
            else:
                return
        else:
            if self.host and self.relative_url:
                url = self.host + self.relative_url + url
            else:
                return
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.content

    def _load_internal(self, tag):
        return '\n'.join(tag.contents)

    def _load_style(self, tag):
        if tag.name == "link":
            return self._load_external(tag)
        elif tag.name == "style":
            return self._load_internal(tag)

    def _load_sheet(self, css_list):
        parser = cssutils.CSSParser()
        self._sheet = parser.parseString(''.join(css_list))
        return self._sheet

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
    
    def convert(self):
        css_list = self._strip_styles()
        self._load_sheet(css_list)
        html = self._apply_rules()
        return str(html)

    def __call__(self):
        return self.convert()

def remove_whitespace(input_string):
    import string
    filtered_string = filter(lambda x: x not in string.whitespace, input_string)
    return filtered_string
