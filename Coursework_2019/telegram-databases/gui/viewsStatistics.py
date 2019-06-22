# import npyscreen
# import analysis
# import filter
#
#
# class ViewsStatistics(npyscreen.ActionForm):
#
#     def create(self):
#         self.value = None
#         self.channels = filter.get_channels_names()
#         self.channel = self.add(npyscreen.TitleMultiLine, name="Channel:", values=self.channels, max_height=4)
#         self.filename = self.add(npyscreen.TitleText, name="Filename:", value='views.png')
#
#     def beforeEditing(self):
#         self.name = "Views statistics"
#
#     def on_ok(self):
#         channel = self.channels[self.channel.value]
#         if filter.is_channel_exist(channel) is not True:
#             npyscreen.notify_confirm(f"channel '{channel}' is not parsed yet", title='Info box')
#         elif self.filename.value == '':
#             npyscreen.notify_confirm("wrong filename", title='Info box')
#         else:
#             message_to_display = 'Processing...\nPicture will be opened in new window...'
#             npyscreen.notify(message_to_display, title='Wait...')
#             analysis.save_views_statistics(channel, self.filename.value)
#             self.parentApp.switchForm("MAIN")
#
#     def on_cancel(self):
#         self.parentApp.switchFormPrevious()
#
#     def exit(self, *args, **keywords):
#         self.parentApp.switchFormPrevious()

import npyscreen
import analysis
import filter


class ViewsStatistics(npyscreen.ActionForm):

    def create(self):
        self.value = None
        self.channels = filter.get_channels_names()
        self.channel = self.add(npyscreen.TitleMultiLine, name="Channel:", values=self.channels, max_height=4)
        self.filename = self.add(npyscreen.TitleText, name="Filename:", value='views.png')

    def beforeEditing(self):
        self.name = "Views statistics"
        self.channels = filter.get_channels_names()
        self.channel.values = self.channels

    def on_ok(self):
        channel = self.channels[self.channel.value]
        if filter.is_channel_exist(channel) is not True:
            npyscreen.notify_confirm(f"channel '{channel}' is not parsed yet", title='Info box')
        elif self.filename.value == '':
            npyscreen.notify_confirm("wrong filename", title='Info box')
        else:
            message_to_display = 'Processing...\nPicture will be opened in new window...'
            npyscreen.notify(message_to_display, title='Wait...')
            analysis.save_views_statistics(channel, self.filename.value)
            self.parentApp.switchForm("MAIN")

    def on_cancel(self):
        self.parentApp.switchFormPrevious()

    def exit(self, *args, **keywords):
        self.parentApp.switchFormPrevious()