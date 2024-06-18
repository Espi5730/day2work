import requests
response = requests.get('https://hacker-news.firebaseio.com/v0/newstories.json')

if response.status_code == 200:
  storys = response.json()
  if storys:
    story = storys[0]
    storyurl = f'https://hacker-news.firebaseio.com/v0/item/{story}.json'
    storyresponse = requests.get(storyurl)
    if storyresponse.status_code == 200:
      story = storyresponse.json()
      title = story.get('title')
      author = story.get('by')
      story_link = story.get('url')       

      print(f"Title: {title}")
      print(f"Author: {author}")
      print(f"Link: {story_link}")