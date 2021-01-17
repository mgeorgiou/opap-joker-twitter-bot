import tweepy
import requests, json
import opapclient
import twitterclient
from datetime import datetime
from chalice import Chalice

three_spaces = "   "
four_spaces = "    "

app = Chalice(app_name='opap-twitter-bot')


@app.route('/')
def index():
    return {'hello': 'world'}


def main():
    results = opapclient.get_last_joker_draw()

    timestamp = datetime.fromtimestamp(results["drawTime"]//1000)
    line_1 = "🗓 ️" + str(timestamp.strftime('%A %d %b %Y'))

    converted_winning_numbers_list = [str(element) for element in results["winningNumbers"]]

    line_2 = three_spaces.join(converted_winning_numbers_list) + four_spaces + "( " + str(results["bonusNumber"]) + " )"
    hashtags = "#τζοκερ #tzoker #οπαπ"

    tweet = line_1 + "\n\n" + line_2 + "\n\n" + hashtags
    print(tweet)

    tweetStatus = twitterclient.postTweet(tweet)

    return {
        'statusCode': 200,
        'body': {'status': tweetStatus}
    }

if __name__ == "__main__":
    main()
