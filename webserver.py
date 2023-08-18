from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from flask import Flask, jsonify
from flask_ngrok import run_with_ngrok
from flask_cors import CORS
import socket
from googleapiclient.http import MediaFileUpload
import os
import cv2
import time

app = Flask(__name__)
CORS(app)
SCOPES = ['https://www.googleapis.com/auth/drive.file']
DOCUMENT_ID = None
HOST = '10.0.0.29'
PORT = 8080
FILENAME = 'received_video8.avi'
FOLDERNAME = 'frames2'

def receive_video():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print('Connected to ESP32-CAM server.')
        with open(FILENAME, 'wb') as f:
            while True:
                data = s.recv(1024)
                print(data)
                if not data:
                    break
                f.write(data)
        print(f'Received video file saved as {FILENAME}.')

def upload_to_drive():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    try:
        service = build('drive', 'v3', credentials=creds)
        folder_metadata = {'name': FOLDERNAME, 'mimeType': 'application/vnd.google-apps.folder'}
        folder = service.files().create(body=folder_metadata, fields='id').execute()
        folder_id = folder.get('id')
        print(f'Folder ID: {folder_id}')
        cap = cv2.VideoCapture(FILENAME)
        frame_count = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
           
            filename = f'frame{frame_count}.jpg'
            cv2.imwrite(filename, frame)
            file_metadata = {'name': filename, 'parents': [folder_id]}
            media = MediaFileUpload(filename, mimetype='image/jpeg')
            service.files().create(body=file_metadata, media_body=media, fields='id').execute()


            print(f'Frame {frame_count} uploaded')
            frame_count += 1
        cap.release()
        print('All frames uploaded successfully')
        
    except HttpError as err:
        print(err)

def get_drive_data():
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    SPREADSHEET_ID = '1U1n17WrhAezcoK_vtrgNVVT7n8l1GBDFmUjQkpmp86w'
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)
        result = service.spreadsheets().values().get(
        spreadsheetId=SPREADSHEET_ID, range='Sheet1').execute()
        values = result.get('values', [])
        
        if not values:
            print('No data found.')
        else:
            k = {}
            i = 0
            for row in values:
                try:
                    k["Name" + str(i)] = row[0]
                    k["Date" + str(i)] = row[1]
                    k["Time" + str(i)] = row[2]
                    i += 1
                except IndexError:
                    continue
    except HttpError as err:
        print(err)
        k = 0
    return k

@app.route("/")

def home(): 
    response = jsonify(k)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
  # receive_video()
  # upload_to_drive()
   k = get_drive_data()
   app.run(host='127.0.0.1', port=8080, debug=True)

