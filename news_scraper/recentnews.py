# Print out all recent news articles

import glob
import json
import pprint
import datetime
import dateutil.parser

# print(glob.glob("*.json"))


def main():
    files = list_files()
    # pprint.pprint(load_json(files[0]))

    js_objs = []
    for filename in list_files():
        js_objs.append(load_json(filename))

    articles = []
    time_delta = datetime.timedelta(days=13)
    for obj in js_objs:
        articles = articles + get_articles_in_timeframe(obj, time_delta)

    # pprint.pprint(articles)
    print_articles(articles)


# list all json files in the current directory
def list_files():
    return glob.glob("*.json")

# take a filename, return a json obj as output
def load_json(filename):
    with open(filename, "r") as f:
        js = f.read()

    js_obj = json.loads(js)
    return js_obj

# Given a json object, return articles within specified time window
def get_articles_in_timeframe(json_obj, time_delta):
    articles = []
    for a in json_obj:
        pub_date = a["date_published"]
        pub_date = dateutil.parser.parse(pub_date)

        now = datetime.datetime.now()
        now = now - time_delta

        if pub_date > now:
            articles.append(a)

    return articles

def print_articles(articles):
    for a in articles:
        print("title: " + a["article_title"])
        print("pub_date: " + a["date_published"])
        print("link: " + a["article_link"])
        print("=================================")

if __name__ == "__main__":
    main()
