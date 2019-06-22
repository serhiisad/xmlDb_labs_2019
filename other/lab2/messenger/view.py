import sys, os
import time
import select
from messenger import storage
# # Main definition - constants
# menu_actions = {}

LOGIN = ""


# =======================
#     MENU FUNCTIONS
# =======================

#general method
def exec_menu(choice, menu_actions):
    os.system('clear')
    ch = choice.lower()
    try:
        menu_actions[ch]()
    except KeyError:
        print("Invalid selection, please try again.\n")


#Exit program
def exit():
    sys.exit()

# #back  to previous menu
# def back(previous_menu):
#     previous_menu()
#



#
def login_menu():
    os.system('clear')

    print("----------Redis - Lab 2 - Log In----------")
    print( "1. as User")
    print ("2. as Admin")
    print ( "\n0. Quit")
    choice = input(" >>  ")

    exec_menu(choice, login_actions)
    return


def user_loginmenu():
    os.system('clear')

    print("----------User - Log In----------")
    print("Type login ")
    login = input(" >>  ")
    logIn(login)
    user_menu()
    return

def admin_loginmenu():
    os.system('clear')

    print("----------ADMIN - Log In----------")
    print("Type login ")
    login = input(" ('admin')>>  ")
    logIn(login)
    admin_menu()
    return


def user_menu():
    os.system('clear')

    print("----------USER----------")
    print("1. sent messages(grouped by status)")
    print("2. received messages\n")
    print("3. SEND a message")

    print("\n0. Back")
    choice = input(" >>  ")

    exec_menu(choice, user_actions)
    return

def admin_menu():
    os.system('clear')

    print("----------ADMIN----------")
    print("1. Users activity")
    print("2. Most active senders")
    print("3. Most frequent spammers")
    print("4. Journal")
    print("\n0. Back")
    choice = input(" >>  ")

    exec_menu(choice, admin_actions)
    return

def sendMessageMenu():
    os.system('clear')

    print("--------SEND message--------\n")
    # print("\nq to return")
    message = input(" message> ")
    channel = input("channel> ")
    sendMessage(LOGIN, channel, message)
    print("\nMessage sent!")
    time.sleep(1)

    user_menu()
    return

# =======================
#     LISTING FUNCTIONS
# =======================


#general method
def listing(getter_funciton):
    while True:
        input = select.select([sys.stdin], [], [], 1)[0]
        if input:
            value = sys.stdin.readline().rstrip()

            if (value == "q"):
                print("Exiting")
                sys.exit(0)
        else:
            list = getter_funciton()
            for el in list:
                print(str(el) + "\n")


def journal_listing():
    os.system('clear')
    print('-------Journal---------(q to return)\n')

    # while True:
    #     input = select.select([sys.stdin], [], [], 1)[0]
    #     if input:
    #         value = sys.stdin.readline().rstrip()
    #
    #         if (value == "q"):
    #             print("Exiting")
    #             sys.exit(0)
    #     else:
    #         list = storage.getJournal()
    #         for el in list:
    #             print(str(el) + "\n")
    listing(getJournal)

    return

def active_users_listing():
    os.system('clear')
    print('---Most active users---(q to return)\n')

    # while True:
    #     input = select.select([sys.stdin], [], [], 1)[0]
    #     if input:
    #         value = sys.stdin.readline().rstrip()
    #
    #         if (value == "q"):
    #             print("Exiting")
    #             sys.exit(0)
    #     else:
    #         list = get
    #         for el in list:
    #             print(str(el) + "\n")
    listing(getActiveSenders)
    return

def active_spammers_listing():
    os.system('clear')
    print('---Most active spammers---(q to return)\n')

    # while True:
    #     input = select.select([sys.stdin], [], [], 1)[0]
    #     if input:
    #         value = sys.stdin.readline().rstrip()
    #
    #         if (value == "q"):
    #             print("Exiting")
    #             sys.exit(0)
    #     else:
    #         list = storage.getActiveSpammers()
    #         for el in list:
    #             print(str(el) + "\n")
    listing(getActiveSpammers)
    return


def received_messages_listing():
    os.system('clear')
    print('---Received messages---(q to return)\n')

    # while True:
    #     input = select.select([sys.stdin], [], [], 1)[0]
    #     if input:
    #         value = sys.stdin.readline().rstrip()
    #
    #         if (value == "q"):
    #             print("Exiting")
    #             sys.exit(0)
    #     else:
    #         list = storage.getReceivedMessages()
    #         for el in list:
    #             print(str(el) + "\n")
    listing(getReceived)
    return


def sent_messages_listing():
    os.system('clear')
    print('---Sent messages---(q to return)\n')

    # while True:
    #     input = select.select([sys.stdin], [], [], 1)[0]
    #     if input:
    #         value = sys.stdin.readline().rstrip()
    #
    #         if (value == "q"):
    #             print("Exiting")
    #             sys.exit(0)
    #     else:
    #         list = storage.getSentMessages()
    #         for el in list:
    #             print(str(el) + "\n")
    listing(getSent)
    return

def activity_listing():
    os.system('clear')
    print('---Activity---(q to return)\n')

    listing(getActivity)
    return

#-------------------------
#login-aware functions ---
#-------------------------

def logIn(login):
    storage.logIn(login)

    print("\n - User Authorized - \n")
    time.sleep(1)
    #todo

def sendMessage(login, channel, message):
    storage.sendMessage(login, channel, message)

    print("\n - Message sent - \n")
    time.sleep(1)
    #todo

# def logOut():
#     storage.logOut(login)
#
#     print("\n - Logged Out - \n")
#     time.sleep(1)
#
#     #todo

def getReceived(login):

    list = storage.getReceivedMessages(login)
    return list

def getSent(login):

    list = storage.getSentMessages(login)
    return list

def getJournal():

    list = storage.getJournal()
    return list

def getActiveSenders():
    list = storage.getMostActiveSenders()
    return list

def getActiveSpammers():
    list = storage.getMostActiveSpammers()
    return list

def getActivity():

    list = storage.getActivity()
    return list


# =======================
#      MENU ACTIONS
# =======================


login_actions = {
    '1': user_loginmenu,
    '2': admin_loginmenu,
    '0': exit,
}

user_actions = {
    '1': sent_messages_listing,
    '2': received_messages_listing,
    '3': sendMessageMenu,

    '0': login_menu,
}

admin_actions = {
    '1': activity_listing,
    '2': active_users_listing,
    '3': active_spammers_listing,
    '4': journal_listing,

    '0': login_menu,
}


# =======================
#      MAIN PROGRAM
# =======================


# Main Program
if __name__ == "__main__":
    # Launch main menu
    login_menu()

def run_ui():
    login_menu()

# #import subprocess
#
# pid = subprocess.Popen(args=[
#     "gnome-terminal", "--command=python test.py"]).pid
# print pid