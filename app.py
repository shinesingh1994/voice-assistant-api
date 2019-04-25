from __future__ import unicode_literals, print_function
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

# Text from Artyom POST request
@app.route('/voice', methods = ['POST'])
@cross_origin(supports_credentials=True)
def parse():

  text = request.form['javascript_data']

  import io
  import json
  import os

  from snips_nlu import SnipsNLUEngine, load_resources
  from snips_nlu.default_configs import CONFIG_EN

  nlu_engine = SnipsNLUEngine.from_path("./nlu_engine")
  parsing = nlu_engine.parse(text)

  return(json.dumps(parsing))

# WaveNet Hype
@app.route('/wavenet', methods = ['POST'])
@cross_origin(supports_credentials=True)
def wavenet():

  text = request.form['text_to_synthesize']
  print(text)

  from google.cloud import texttospeech
  from google.oauth2 import service_account
  import os
  import sys
  from pydub import AudioSegment

# import credentials from google dev api(s)
  credentials = service_account.Credentials.from_service_account_file('./auth.json')

  client = texttospeech.TextToSpeechClient(credentials=credentials)

  synthesis_input = texttospeech.types.SynthesisInput(text=text)

  voice = texttospeech.types.VoiceSelectionParams(
      language_code='en-GB',
      ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

  audio_config = texttospeech.types.AudioConfig(
      audio_encoding=texttospeech.enums.AudioEncoding.MP3)

  response = client.synthesize_speech(synthesis_input, voice, audio_config)

  return(response.audio_content)
