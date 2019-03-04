import pygtkcompat

import gtk

from .commands import ChangeValue
from .scrolled_window import ScrolledWindow

pygtkcompat.enable()
pygtkcompat.enable_gtk(version='3.0')


class TextEditor(gtk.Window):
    def __init__(self, obj, attr):
        super(TextEditor, self).__init__()
        self.obj = obj
        self.attr = attr
        self.set_title("Editing %s.%s" % (repr(obj), attr))
        self.set_default_size(400, 600)
        self.connect('destroy', self.on_close)

        self.text = gtk.TextView()
        text_buffer = self.text.get_buffer()
        text_buffer.set_text(getattr(obj, attr))

        self.add(ScrolledWindow(self.text))
        self.show_all()

    def on_close(self, _):
        text_buffer = self.text.get_buffer()
        start, end = text_buffer.get_bounds()
        text = text_buffer.get_text(start, end)
        cmd = ChangeValue(object=self.obj, attr=self.attr, new_value=text)
        cmd()
