import urwid

login_choices = ["As user", "As admin"]
user_choices = ["write a message", "view received", "view sent messages(grouped by status)"]
admin_choices = ["view online users", "view top spammers", "view top active senders", "view LOG"]

def add_exit_button(body):
    space = urwid.Text("\n")
    body.append(space)
    button_exit = urwid.Button("EXIT")
    urwid.connect_signal(button_exit, 'click', exit_program)
    body.append(urwid.AttrMap(button_exit, None, focus_map='reversed'))

def login_menu(title, choices):
    body = [urwid.Text(title), urwid.Divider()]
    methods = [login_asuser, login_asadmin]

    for i in range(len(choices)):
        button = urwid.Button(choices[i])
        urwid.connect_signal(button, 'click', methods[i], choices[i])
        body.append(urwid.AttrMap(button, None, focus_map='reversed'))
    # button1 = urwid.Button(choices[0])
    # button2 = urwid.Button(choices[1])
    #
    # urwid.connect_signal(button1, 'click', login_asuser, choices[0])
    # urwid.connect_signal(button2, 'click', login_asadmin, choices[1])
    #
    # body.append(urwid.AttrMap(button1, None, focus_map='reversed'))
    # body.append(urwid.AttrMap(button2, None, focus_map='reversed'))

    add_exit_button(body)

    return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def user_menu(title, choices):
     body = [urwid.Text(title), urwid.Divider()]
     methods = [write_message, view_received, view_sent]

     for i in range(len(choices)):
         button = urwid.Button(choices[i])
         urwid.connect_signal(button, 'click', methods[i], choices[i])
         body.append(urwid.AttrMap(button, None, focus_map='reversed'))
     # button1 = urwid.Button(choices[0])
     # button2 = urwid.Button(choices[1])
     # button3 = urwid.Button(choices[2])
     #
     # urwid.connect_signal(button1, 'click', write_message, choices[0])
     # urwid.connect_signal(button2, 'click', view_received, choices[1])
     # urwid.connect_signal(button1, 'click', view_sent, choices[2])
     #
     # body.append(urwid.AttrMap(button1, None, focus_map='reversed'))
     # body.append(urwid.AttrMap(button2, None, focus_map='reversed'))
     # body.append(urwid.AttrMap(button1, None, focus_map='reversed'))

     add_exit_button(body)

     return urwid.ListBox(urwid.SimpleFocusListWalker(body))


def admin_menu(title, choices):
    body = [urwid.Text(title), urwid.Divider()]
    methods = [view_online_users, view_spammers, view_active_users, view_log]

    for i in range(len(choices)):
        button = urwid.Button(choices[i])
        urwid.connect_signal(button, 'click', methods[i], choices[i])
        body.append(urwid.AttrMap(button, None, focus_map='reversed'))

    add_exit_button(body)

    return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def login_asuser(button, choice):

    response = urwid.Text([u'type login ', choice, u'\n'])

    login_edit = urwid.Edit("Login> \n")
    # fill = urwid.Filler(login_edit)

    login = login_edit.get_text()
    print("TEXT", login)

    submit = urwid.Button(u'Ok')
    urwid.connect_signal(submit, 'click', exit_program)
    login_main.original_widget = urwid.Filler(urwid.Pile([response,
                                                     urwid.AttrMap(submit, None, focus_map='reversed')]))
    #
    # loop = urwid.MainLoop(fill)
    # loop.run()

def login_asadmin(button, choice):
    response = urwid.Text([u'type admin name(admin) ', choice, u'\n'])
    login_edit = urwid.Edit(u"Login(admin): ")
    submit = urwid.Button(u'Ok')
    urwid.connect_signal(submit, 'click', exit_program)
    login_main.original_widget = urwid.Filler(urwid.Pile([response,
                                                          urwid.AttrMap(submit, None, focus_map='reversed')]))

#TODO
def write_message():
    pass

def view_received():
    pass

def view_sent():
    pass

def view_spammers():
    pass

def view_online_users():
    pass

def view_active_users():
    pass

def view_log():
    pass

def exit_program(button):
    raise urwid.ExitMainLoop()

#TODO
def exit_menu(button):
    pass

login_main = urwid.Padding(login_menu('Redis_Lab2 - Log in', login_choices), left=2, right=2)
user_main = urwid.Padding(user_menu('User', user_choices), left=2, right=2)
admin_main = urwid.Padding(admin_menu('Admin', admin_choices), left=2, right=2)
#todo

login_top = urwid.Overlay(login_main, urwid.SolidFill(u'\N{MEDIUM SHADE}'),
                        align='center', width=('relative', 60),
                        valign='middle', height=('relative', 60),
                        min_width=20, min_height=9)

#RUN UI
urwid.MainLoop(login_top, palette=[('reversed', 'standout', '')]).run()



