import streamlink, urllib, re, praw, time, datetime, os, warnings, config
from urllib.request import Request, urlopen
from random import randint
from datetime import datetime

# Connect to Reddit account
reddit = praw.Reddit(
    client_id=config.client_id,
    client_secret=config.client_secret,
    user_agent=config.user_agent,
    username=config.username,
    password=config.password,
)

# Timestamp for terminal
now = datetime.now()
current_time = now.strftime("%I:%M:%S %p")

# Path to broadcasts.txt
broadcasts_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'broadcasts.txt')

# Livestream
try_stream=streamlink.streams(config.channel_link)
# Livestream page
livestream_page=urllib.request.urlopen(config.channel_link)
# Livestream page as bytes
livestream_page_bytes=bytes(livestream_page.read())
# Decoded bytes
livestream_page_decoded=livestream_page_bytes.decode('utf-8')
# YouTube livestream URL
livestream_url=livestream_page_decoded.split('="canonical" href="',1)[1].split('"',1)[0]

# Posts subreddit submission
def submit():
    # Subreddit to post submissions in
    subreddit=reddit.subreddit(config.subreddit_name)
    # Posts submission
    subreddit.submit(config.submission_title,url=config.url,flair_id=config.flair)
    # Sleeps before stickying to avoid Bad Request from server latency
    time.sleep(randint(5,10))

# Stickies submission
def sticky():
    # Most recent submission in user history
    for submission in reddit.redditor(config.username).submissions.new(limit=1):
        submission.mod.sticky(True)

# Deletes most recent user submission
def delete():
    # Most recent submission in user history as a list
    submission_list = list(reddit.redditor(config.username).submissions.new(limit=1))

    # Submission doesn't exist
    if not submission_list:
        pass

    # Submission exists
    else:
        
        for submission in submission_list:
            submission.delete()
            print("["+current_time+"] Previous submission removed")

# Delete url data
def clean():
    del livestream_page, livestream_page_bytes, livestream_page_decoded, livestream_url
    
    # Delete scheduledTime if defined
    try:
        del scheduledTime
    except NameError:
        pass


# Try to connect to livestream
try:
    stream = try_stream["best"]

# Fail to connect to livestream
except:

    # Try to grab unix timestamp for scheduled livestream
    try:
        # Unix timestamp for scheduled livestream
        scheduledTime = re.search('"scheduledStartTime":"(.+?)",', livestream_page_decoded).group(1)

    # Livestream doesn't exist
    except:
        # Delete url data
        clean()
        # Delete most recent user submission
        delete()
        print("["+current_time+"] Stream offline, sleeping...")

    # Livestream is scheduled
    else:
        # Delete url data
        clean()
        print("["+current_time+"] Stream soon, sleeping...")

# Livestream exists
else:

    # Opens broadcasts.txt to read
    with open(broadcasts_path, "r+",) as broadcasts_read:
        # Read broadcasts.txt
        contents = broadcasts_read.read()

        # Searches for livestream URL in broadcasts.txt
        if contents.find(livestream_url) != -1:
            print("["+current_time+"] Submission has already been posted, sleeping... ")
            # Closes file
            broadcasts_read.close()
            # Delete url data
            clean()

        # Livestream URL not found in broadcasts.txt
        else:
            # Closes file
            broadcasts_read.close()
            # Deletes most recent user submission
            delete()
            print("["+current_time+"] Posting submission")

            # Opens broadcasts.txt to append
            with open(broadcasts_path, "a") as broadcasts_append:
                # Writes livestream URL into broadcasts.txt
                broadcasts_append.write("\n"+livestream_url)
                # Closes file
                broadcasts_append.close()
                # Posts subreddit submission
                submit()

                # Tries to connect to first subreddit sticky
                try:
                    # Top posts in subreddit
                    for submission in reddit.subreddit(config.subreddit_name).hot():
                        # First sticky
                        sticky_1=str(reddit.subreddit(config.subreddit_name).sticky(1))

                # No stickies exist
                except:
                    # Stickies submission
                    sticky()
                    # Delete url data
                    clean()
                    print("["+current_time+"] Submission has been posted and stickied, sleeping...")

                # First sticky exists
                else:

                    # Tries to connect to second subreddit sticky
                    try:
                        # Top posts in subreddit
                        for submission in reddit.subreddit(config.subreddit_name).hot():
                            # Second sticky
                            sticky_2=str(reddit.subreddit(config.subreddit_name).sticky(2))

                    # Second sticky doesn't exist
                    except:
                        # Stickies submission
                        sticky()
                        # Delete url data
                        clean()
                        print("["+current_time+"] Submission has been posted and stickied, sleeping...")
                    
                    # Second sticky exists
                    else:
                        # Delete url data
                        clean()
                        print("["+current_time+"] No sticky slots, an unstickied submission has been posted, sleeping...")