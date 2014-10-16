import re
import requests

graph = 'https://graph.facebook.com'
app_user_id = '375991845883325' # Strażnik Tagów @ Tag Nazi
group_id = '1508885209354773'
access_token = open('access_token').read()
payload = { 'access_token': access_token }
tag_regex = r'(\[\w+\])'
warning_text = 'Twój post nie jest otagowany!'

url = graph + '/%s/feed' % group_id
r = requests.get(url, params=payload)
feed = r.json()
for post in feed['data']:
    post_id = post['id']
    message = post['message']
    print(post_id, '"%s"' % message)
    is_tagged = re.match(tag_regex, message)
    if not is_tagged:
        print('not tagged')
        try:
            comments = post['comments']['data']
            commenters = [c['from']['id'] for c in comments]
        except KeyError:
            commenters = []
        if not app_user_id in commenters:
            print('adding comment')
            payload['message'] = warning_text
            r = requests.post(graph + '/%s/comments' % post_id, payload)
            print('response:', r.text)