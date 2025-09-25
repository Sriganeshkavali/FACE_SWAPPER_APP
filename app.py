# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
from image_process import initialize_models, process_images_for_swap

# Configuration
UPLOAD_FOLDER = os.path.join('static', 'uploads')
RESULTS_FOLDER = os.path.join('static', 'results')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULTS_FOLDER'] = RESULTS_FOLDER
app.secret_key = 'supersecretkey'

app_model, swapper_model = initialize_models()

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(RESULTS_FOLDER):
    os.makedirs(RESULTS_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/swap', methods=['POST'])
def swap_faces():
    if 'image1' not in request.files or 'image2' not in request.files:
        flash('Please upload both images!')
        return redirect(url_for('index'))

    file1 = request.files['image1']
    file2 = request.files['image2']

    if file1.filename == '' or file2.filename == '':
        flash('Please select both files!')
        return redirect(url_for('index'))

    if file1 and allowed_file(file1.filename) and file2 and allowed_file(file2.filename):
        filename1 = secure_filename(file1.filename)
        filename2 = secure_filename(file2.filename)
        filepath1 = os.path.join(app.config['UPLOAD_FOLDER'], filename1)
        filepath2 = os.path.join(app.config['UPLOAD_FOLDER'], filename2)
        
        file1.save(filepath1)
        file2.save(filepath2)

        # process_images_for_swap needs to return web-friendly paths or just filenames
        output_path1, output_path2 = process_images_for_swap(filepath1, filepath2, app_model, swapper_model)

        if output_path1 is None:
            flash('Faces were not detected in one of the images. Please try again with different pictures.')
            return redirect(url_for('index'))

        # Extract just the filenames to pass to the template
        swapped_filename1 = os.path.basename(output_path1)
        swapped_filename2 = os.path.basename(output_path2)
        
        return render_template(
            'index.html',
            original_img1=filename1,
            original_img2=filename2,
            swapped_img1=swapped_filename1,
            swapped_img2=swapped_filename2
        )
    else:
        flash('Invalid file type. Only PNG, JPG, and JPEG are allowed.')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)