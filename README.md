# AldensBot
**"Are you familiar with Alden's bot?" - [Vaush](https://www.youtube.com/@Vaush)**

### About
AldensBot is a simple Python program that automatically posts, stickies, and removes YouTube livestream notifications to Reddit.

Please do not use this program in it's current state, as it was only created for development purposes, and I am currently developing an alternative that uses YouTube's API.

### Installation and Usage
1. Create an [app](https://www.reddit.com/prefs/apps) for the Reddit account that will be used
2. Download the AldensBot repository
3. Install dependencies
```
pip install streamlink
pip install praw
```
4. Setup `config.py`
5. Run `main.py`

### Configuration
- client_id
    - Client ID for Reddit app, found [here](https://www.reddit.com/prefs/apps) near app icon
- client_secret
    - Client secret for Reddit app, found [here](https://www.reddit.com/prefs/apps)
- user_agent
    - User agent for Reddit app, example: `https://github.com/thaena/AldensBot by u/you`
- username
    - Username for Reddit account
- Password
    - Password for Reddit account
- channel_link
    - Live link for YouTube channel, example: `https://www.youtube.com/@Vaush/live`
- subreddit_name
    - Subreddit that will be posted into
- url
    - URL that will be included in submissions when posted
- submission_title
    - Title that will be included in submissions when posted
- flair (optional)
    - Subreddit flair ID that will be added to submissions, found in subreddit mod tools
    - No flair will be added if variable is left empty
