import discord
from db import get_session
from model import Emoji_info
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os


#---------------日曆 utils---------------------#

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly', 'https://www.googleapis.com/auth/calendar']
service = None

async def calendar_setting():

    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)
    except HttpError as error:
        print('An error occurred: %s' % error)
    
    return service

#---------------點數 utils---------------------#
async def get_points_message(points : int, query : bool):

    session = get_session()

    emoji_number = ""
    for char in str(points):
        emoji = session.query(Emoji_info).filter(Emoji_info.emoji_name == char).first()
        emoji_number += f"<:{emoji.emoji_eng}:{emoji.emoji_id}>"

    if query: 
        return f"您的 G token 目前已累積 {points} :coin:\n{emoji_number}"

    else:
        return f"您醬獲得了 {points} :coin:\n{emoji_number}"


#---------------點飲料 utils---------------------#

async def update_data(users, user, item):
    if 'TodayOrder' not in users:
        users['TodayOrder'] = []
    else:
        pass

    return users

async def add_content(users, user, name, item, sugar, ice):
    print(name, item, sugar, ice)
    nameS = name
    users['TodayOrder'].append(
        {"Name": nameS, "item": item, "Sugar": sugar, "ice": ice})
    
    return users