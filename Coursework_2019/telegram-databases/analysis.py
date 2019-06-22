import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import collections
from collections import defaultdict
from stop_words import get_stop_words

import filter
import pymorphy2
from nltk.corpus import stopwords
from nltk import word_tokenize
morph = pymorphy2.MorphAnalyzer()
from collections import Counter

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

from itertools import groupby

weekdays_list = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
ukrainian_stop_words = get_stop_words('ukrainian')

path_to_pictures = "pictures/"
if not os.path.exists(path_to_pictures):
    os.makedirs(path_to_pictures)

def get_colors(n):
    colors = []
    cm = plt.cm.get_cmap('tab10', n)
    for i in np.arange(n):
        colors.append(cm(i))
    return colors


def normalize_word(word):
    w = morph.parse(word)[0]
    return w.normal_form


def prepare_messages(messages):
    prepared = []
    for message in messages:
        words = word_tokenize(str.lower(message))
        normalized = [normalize_word(word) for word in words
            if word.isalpha()
                      and word not in stopwords.words("russian")
                      and word not in ukrainian_stop_words
                      and word != "https" and word != "https"] # to delete links
        if len(normalized) > 0:
            prepared.append(normalized)

    toReturn = []
    for sentence in prepared:
        toReturn += sentence
    #     toReturn = [' '.join(word for word in sentence) for sentence in prepared]
    return toReturn


def save_popular_messages_words(channel_name, filename):
    messages = filter.get_all_messages(channel_name)
    messages_count = 0
    msg_list = []
    for msg in messages:
        msg_list.append(msg["message"])
        messages_count += 1
    messages = prepare_messages(msg_list)
    # print(messages)

    words = dict(Counter(messages).most_common(10))

    dict_keys = list(words.keys())
    dict_values = list(words.values())
    top_keys = len(words)

    plt.subplots_adjust(left=0.1, right=0.9, bottom=0.25, top=0.9)
    plt.title(f'Most common words in posts (processed {messages_count} posts from @{channel_name})', fontsize=10)
    plt.bar(np.arange(top_keys), dict_values, color=get_colors(top_keys))
    plt.xticks(np.arange(top_keys), dict_keys, rotation=90, fontsize=10)
    plt.yticks(fontsize=10)
    plt.ylabel('Number of entries', fontsize=10)

    fig = plt.gcf()
    fig.set_size_inches(16, 9)
    plt.savefig(path_to_pictures + filename)
    plt.show()


def save_views_statistics(channel_name, filename):
    data = filter.get_channel_views(channel_name)
    lst = []
    for obj in data:
        lst.append({
            'date': str(obj["date"].date()),
            'views': int(obj["views"])
        })

    lst.sort(key=lambda x: x['date'][:7])
    # print(lst)
    groupby(lst, key=lambda x: x['date'][:7])

    df = pd.DataFrame(columns=['date', 'views'])
    for k, v in groupby(lst, key=lambda x: x['date'][:7]):
        df = df.append({'date': k + '-01', 'views': sum(int(d['views']) for d in v)}, ignore_index=True)

    df = df.sort_values('date', ascending=True)
    df['date'] = pd.to_datetime(df['date'])

    plt.plot(df['date'], df['views'])
    plt.xticks(rotation='horizontal')

    plt.ticklabel_format(style='plain', axis='y')
    plt.title(f'Views of @{channel_name}', fontsize=10)
    plt.yticks(fontsize=10)
    plt.ylabel('Views per month', fontsize=10)

    fig = plt.gcf()
    fig.set_size_inches(16, 9)
    plt.savefig(path_to_pictures + filename)
    plt.show()


def sort_dates_by_weekday(dates):
    result = defaultdict(int)
    current_day = -1
    prev_day = current_day
    days_number = 0
    weeks_number = 0
    for obj in dates:
        weekday = obj["date"].weekday()
        current_day = weekday
        result[weekday] = result[weekday] + 1

        if (current_day != prev_day):
            days_number += 1

        if (days_number == 6):
            weeks_number +=1
            days_number = 0
        prev_day = current_day

    result = collections.OrderedDict(sorted(result.items()))
    for key, value in result.items():
        result[key] = value/weeks_number

    return (weeks_number, dict(result))


def save_weekdays_statistics(channel_name, filename):
    dates = filter.get_channel_posts_dates(channel_name)
    weeks_number, dates = sort_dates_by_weekday(dates)
    dict_values = list(dates.values())
    dict_keys = list(map(lambda x: "{}".format(weekdays_list[x]), dates))
    top_keys = len(dates)

    plt.title(f'Average number of posts per weekdays(@{channel_name} for {weeks_number} weeks)', fontsize=10)
    plt.bar(np.arange(top_keys), dict_values, color=get_colors(top_keys))
    plt.xticks(np.arange(top_keys), dict_keys, rotation=90, fontsize=10)
    plt.yticks(fontsize=10)
    plt.ylabel('Number of posts', fontsize=10)
    fig = plt.gcf()
    fig.set_size_inches(16, 9)
    plt.savefig(path_to_pictures + filename)
    plt.show()


# save_popular_messages_words("kpilive", "top10words.png")
# save_views_statistics("kpilive", "total_views.png")
# save_weekdays_statistics("kpilive", "weekdays_posts.png")
