import npyscreen
from database import database
from gui import mainList, popularWords, weekdayStatistics, viewsStatistics, parse


class App(npyscreen.NPSAppManaged):
    def __init__(self, *args, **keywords):
        super().__init__(*args, **keywords)
        self.db = database.connect()

    def onStart(self):
        self.addForm("MAIN", mainList.MainListDisplay, title='Main menu')
        self.addForm("PARSE", parse.Parse, title='Parse')
        self.addForm("POPULAR_WORDS", popularWords.PopularWords, title='Popular words')
        self.addForm("WEEKDAY_STATISTICS", weekdayStatistics.WeekdayStatistics, title='Weekday statistics')
        self.addForm("VIEWS_STATISTICS", viewsStatistics.ViewsStatistics, title='Views statistics')

    def onCleanExit(self):
        # self.database.close()
        pass

if __name__ == '__main__':
    MyApp = App()
    MyApp.run()