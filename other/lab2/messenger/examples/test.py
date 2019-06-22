import urwid
#
# txt = urwid.Text(u"Hello World")
# fill = urwid.Filler(txt, 'top')
# loop = urwid.MainLoop(fill)
# loop.run()

def show_or_exit(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()
    txt.set_text(repr(key))

txt = urwid.Text(u"Hello World")
fill = urwid.Filler(txt, 'top')
loop = urwid.MainLoop(fill, unhandled_input=show_or_exit)
loop = urwid.MainLoop(fill)
loop.run()

