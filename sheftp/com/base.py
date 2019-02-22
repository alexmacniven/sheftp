class Base(object):
    """The base command"""
    def __init__(self, options, *args, **kwargs):
        """Constructor"""
        self.options = options
        self.args = args
        self.kwargs = kwargs

    def run(self):
        """Base run function"""
        raise NotImplementedError