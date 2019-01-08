

import glob
import json
import pprint
import datetime
import dateutil.parser


def main():
    craft_html(4)

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
    if len(articles) > 0:
        print("SOURCE: " + articles[0]["source"])
    for a in articles:
        print("title: " + a["article_title"])
        print("pub_date: " + a["date_published"])
        print("link: " + a["article_link"])
        print("=================================")

def print_articles2(articles):
    for a in articles:
        print(a["date_published"] + " " + a["source"] + " " + a["article_title"])
        print(a["article_link"])
        print("===================")

def craft_html_from_articles(articles):
    html_str = "<!doctype html><html lang=\"en\"><body>"
    # html_articles = []
    for a in articles:
        a_str = "<h3><a href=\"{}\">{}: {}</a></h3>".format(a["article_link"], a["source"], a["article_title"])
        a_str = a_str + "<p>{}</p><p>{}</p>".format(a["date_published"], a["short_description"])
        # html_articles.append(a_str)
        html_str = html_str + a_str
    html_str = html_str + "</body></html>"
    with open("articles.html", "w") as f:
        f.write(html_str)
        f.flush()
        f.close()

def craft_html(days_back):
    files = list_files()

    js_objs = []
    for filename in list_files():
        js_objs.append(load_json(filename))

    articles = []
    time_delta = datetime.timedelta(days=days_back)
    for obj in js_objs:
        articles = articles + get_articles_in_timeframe(obj, time_delta)
    craft_html_from_articles(articles)



if __name__ == "__main__":
    main()
