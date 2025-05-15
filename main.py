import os
import shutil
import sys
script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
source_dir = script_directory
target_dirs = {
    'Documents': ['.doc', '.docx', '.pdf'],
    'Presentations': ['.ppt','.pptx'],
    'Pictures': ['.jpg','.png'],
    'Audios': ['.mp3','.wav','.aac','.m4a'],
    'Videos': ['.mp4','.mov','.avi','.wmv'],
    'shortcuts': ['.lnk'],
    'Python files': ['.py'],
    'Web files': ['.html','.css'],
    'Applications': ['.exe'],
    'Compressed': ['.zip','.rar','.gz']
}

for folder in target_dirs:
    os.makedirs(os.path.join(source_dir, folder), exist_ok=True)
for filename in os.listdir(source_dir):
    filepath = os.path.join(source_dir, filename)
    if os.path.isdir(filepath):
        continue   
    _, ext = os.path.splitext(filename)
    for folder, extensions in target_dirs.items():
        if ext.lower() in extensions:
            shutil.move(filepath, os.path.join(source_dir, folder, filename))
            break
