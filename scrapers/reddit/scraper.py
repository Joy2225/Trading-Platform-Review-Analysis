import praw
from googlesearch import search
import duckdb
import credentials

reddit = praw.Reddit(client_id=credentials.client_id, client_secret=credentials.client_secret,
                     user_agent=credentials.user_agent, username=credentials.username, password=credentials.password)

def get_comments(url, replace_more_comments=False):
    submission = reddit.submission(url=url)
    if replace_more_comments:
        submission.comments.replace_more(limit=0)
    return submission.comments.list()

def store_comments_in_duckdb(comments, app_name, conn):
    for comment in comments:
        try:
            conn.execute("INSERT INTO comments_table VALUES (?, ?)", (app_name, comment.body))
        except AttributeError:
            continue

def main():
    apps = ["Zerodha Kite", "Groww", "Upstox", "Paytm Money", "Dhani Stocks", "Motilal Oswal", "Angel Broking", "Sharekhan", "Nuvama", "HDFC Securities"]

    conn = duckdb.connect(database=':memory:')
    conn.execute("""
        CREATE TABLE IF NOT EXISTS comments_table (
            app_name TEXT,
            comment TEXT
        );
    """)

    for app in apps:
        search_query = f"{app} site:www.reddit.com"
        reddit_urls = list(search(search_query, num_results=10))

        for url in reddit_urls:
            if 'reddit.com/r/' in url:
                comments = get_comments(url)
                store_comments_in_duckdb(comments, app_name=app, conn=conn)

    csv_file = "../../data/trading_apps_comments.csv"
    conn.execute(f"COPY comments_table TO '{csv_file}' (FORMAT 'csv', HEADER TRUE)")

    conn.close()

if __name__ == "__main__":
    main()
