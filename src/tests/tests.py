class TestCase(object):
    def setup(self):
        f = open('test.html','r')
        self.html = f.read()
        f.close()
    
    def test_style_striping(self):
        #assert self.html has no style attributes
        from inlinestyle import do_work
        do_work(self.html)
        assert False
    