import os
from flask import Flask, request, render_template, send_file
from home_work_v2 import write_home_work  # Import the home_work_write function from v2.py

app = Flask("home_work_write")

# Directory for storing generated images
OUTPUT_DIR = "D:\\assignments\\MC\\5m"

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_images():
    text_file = request.files['text_file']

    if text_file:
        # Save the uploaded text file
        text_file_path = os.path.join(OUTPUT_DIR, text_file.filename)
        text_file.save(text_file_path)

        # Call the home_work_write function with the text file and output directory
        write_home_work(text_file_path, OUTPUT_DIR)

        # Provide a link to download the generated image(s)
        return f'Images generated successfully! <a href="/download/{text_file.filename}">Download Images</a>'

    return 'No text file uploaded.'

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join(OUTPUT_DIR, filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
