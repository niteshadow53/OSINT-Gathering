from jinja2 import Environment, FileSystemLoader, select_autoescape
import glob
import json
import datetime
import dateutil.parser
import pprint

def main():
    output_filepath = "html/articles_jinja_output.html"
    env = Environment(
        loader = FileSystemLoader('templates/'),
        autoescape = select_autoescape(['html', 'xml'])
    )

    template = env.get_template('article_view.html')

    js_objs = collect_articles()
    articles=get_articles_in_timeframe(js_objs, 2)

    html_output_str = template.render(articles=articles)
    with open(output_filepath, "w") as file_:
        file_.write(html_output_str)
        file_.flush()
        file_.close()

# list all json files in the current directory
def list_files():
    return glob.glob("*.json")

# take a filename, return a json obj as output
def load_json(filename):
    with open(filename, "r") as f:
        js = f.read()

    js_obj = json.loads(js)
    return js_obj

# Return js object of all articles collected from all files
def collect_articles():
    files = list_files()

    js_objs = []
    for filename in list_files():
        js_objs = js_objs + load_json(filename)

    # pprint.pprint(js_objs)
    return js_objs

# Given a json object, return articles as json objects within specified time window
def get_articles_in_timeframe(json_obj, days_back):
    articles = []
    for a in json_obj:
        pub_date = a["date_published"]
        pub_date = dateutil.parser.parse(pub_date)

        now = datetime.datetime.now()
        time_delta = datetime.timedelta(days=days_back)
        now = now - time_delta

        if pub_date > now:
            articles.append(a)

    return articles

if __name__ == "__main__":
    main()
