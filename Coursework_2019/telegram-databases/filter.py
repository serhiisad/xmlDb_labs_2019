from database import database

db = database.connect()


def get_all_messages(channel_name):
    return db.messages.aggregate([
        {
            "$match": {
                "channel": channel_name,
            }
        },
        {
            "$project": {
                "_id": 0,
                "message": 1,
            }
        }
    ])
    # return db.messages.distinct("message")


def get_channel_views(channel_name):
    return db.messages.aggregate([
        {
            "$match": {
                "channel": channel_name,
                "date": {
                    "$exists": True
                }
            }
        },
        {
            "$project": {
                "_id": 0,
                "date": 1,
                "views": 1
            }
        }
    ])


def get_channel_posts_dates(channel_name):
    return db.messages.aggregate([
        {
            "$match": {
                "channel": channel_name,
                "date": {
                    "$exists": True
                }
            }
        },
        {
            "$project": {
                "_id": 0,
                "date": 1
            }
        }
    ])


def is_channel_exist(channel_name):
    return db.messages.count({"channel": channel_name}) != 0


def get_channels_names():
    return db.messages.distinct("channel")


def remove_channel(channel_name):
    return db.messages.remove({
        "channel": channel_name
    })

# res = get_channel_views()
# for obj in res:
#     print(obj)