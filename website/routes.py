from flask import Blueprint, render_template, request, jsonify
import os

routes = Blueprint("routes", __name__)

@routes.route("/")
def index():
    return render_template("index.html")


@routes.route("/webcam")
def webcam():
    return render_template("webcam.html")


@routes.route("/upload-recording", methods=["POST"])
def upload_recording():
    
    #Looking for a file named video is not returning an error message
    if "video" not in request.files:
        return jsonify({"message": "No video uploaded."}), 400
    
    #Getting the video file 
    video = request.files["video"]
    
    #Saving the video file into this path 
    os.makedirs("data/videos", exist_ok=True)
    filepath = os.path.join("data/videos", "recording.webm")
    video.save(filepath)
    
    #Returning a success message
    return jsonify({"message": "Recording successfully uploaded."})