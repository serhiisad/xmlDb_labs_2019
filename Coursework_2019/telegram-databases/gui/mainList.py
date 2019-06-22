import npyscreen
import analysis
import sys
from database import database

values_list = ['Parse channel',
               'Get top 10 popular words in messages',
               'Get weekday statistic',
               'Get views statistic',
               'Import database',
               'Export database',
               'Exit']

class MainList(npyscreen.MultiLineAction):
    def __init__(self, *args, **keywords):
        super(MainList, self).__init__(*args, **keywords)
        self.name = "Main List"


    def display_value(self, vl):
        return "{:^80}".format(str(vl))


    def actionHighlighted(self, act_on_this, keypress):
        self.spawn_notify_popup(act_on_this)

    def spawn_notify_popup(self, entity):

        index = values_list.index(entity)
        func = None
        if (index == 0):
            return self.parent.parentApp.switchForm("PARSE")
        elif (index == 1):
            return self.parent.parentApp.switchForm("POPULAR_WORDS")
        elif (index == 2):
            return self.parent.parentApp.switchForm("WEEKDAY_STATISTICS")
        elif (index == 3):
            return self.parent.parentApp.switchForm("VIEWS_STATISTICS")
        elif (index == 4):
            func = database.import_collection
        elif (index == 5):
            func = database.export_collection
        elif (index == 6):
            self.parent.parentApp.switchForm(None)
            sys.exit(0)
        message_to_display = 'Processing...\nPicture will be opened in new window...'
        npyscreen.notify(message_to_display, title='Wait...')
        func()
        self.parent.parentApp.switchForm("MAIN")


class MainListDisplay(npyscreen.FormMutt):

    MAIN_WIDGET_CLASS = MainList

    def __init__(self, *args, **keywords):
        super().__init__(*args, **keywords)
        self.add_handlers({
            "^Q": self.exit
        })

    def beforeEditing(self):
        self.wMain.values = values_list
        self.wMain.display()

    def exit(self, *args, **keywords):
        self.parentApp.switchForm(None)