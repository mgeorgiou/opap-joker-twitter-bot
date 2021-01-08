import tweepy
import requests, json
import opapclient
import twitterclient
from datetime import datetime

three_spaces = "   "
four_spaces = "    "

def main():
    results = opapclient.get_last_joker_draw()

    timestamp = datetime.fromtimestamp(results["drawTime"]//1000)
    line_1 = "🗓 ️" + str(timestamp.strftime('%A %d %b %Y'))

    converted_winning_numbers_list = [str(element) for element in results["winningNumbers"]]

    line_2 = three_spaces.join(converted_winning_numbers_list) + four_spaces + "( " + str(results["bonusNumber"]) + " )"
    hashtags = "#τζοκερ #tzoker #οπαπ"

    tweet = line_1 + "\n\n" + line_2 + "\n\n" + hashtags
    print(tweet)

    twitterclient.postTweet(tweet)

if __name__ == "__main__":
    main()
