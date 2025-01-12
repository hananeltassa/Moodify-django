import os

def save_uploaded_file(file, upload_dir='uploads/voice_files/'):
    """Save the uploaded voice file to a specific directory."""
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    file_path = os.path.join(upload_dir, file.name)
    with open(file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return file_path
