import os

import requests

from flask import Flask, render_template

NASA_URL = "https://api.nasa.gov/planetary/apod?api_key={...}"

app = Flask(__name__)

@app.route('/')
def anchor():
    response = requests.get(NASA_URL).json()

    copyright_text = "Image Credits:"
    if copyright in response:
        copyright_text += response['copyright']
    else:
        copyright_text += "Public Domain"

    description_text = response.get('explanation', 'No description')
    title_text = response.get('title', 'No title')

    media_type = response['media_type']
    media_url = response['url']

    return render_template(
        'index.html',
        media_type=media_type,
        media_url=media_url,
        title_text=title_text,
        copyright_text=copyright_text,
        description_text=description_text
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5001)




