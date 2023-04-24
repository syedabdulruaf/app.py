import facebook
import streamlit as st

# Get your App ID and App Secret from the Facebook Developers website
app_id = 'YOUR_APP_ID'
app_secret = 'YOUR_APP_SECRET'

# Create a Facebook Graph API object
graph = facebook.GraphAPI(access_token=f'{app_id}|{app_secret}', version='3.0')

# Get the user's profile picture and name
profile = graph.get_object('me', fields='id,name,picture')
st.image(profile['picture']['data']['url'])
st.write(f'Name: {profile["name"]}')

# Get the user's friends
friends = graph.get_connections('me', 'friends')['data']
st.write('Friends:')
for friend in friends:
    st.write(friend['name'])
