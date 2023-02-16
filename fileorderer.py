import os
import shutil

# Define the path to the documents folder
documents_path = "Q:/Users/t_kurtulus1/Downloads"

# Define the categories and their corresponding file extensions
categories = {
    "Images": [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".bmp", ".dib", ".svg", ".svgz", ".ico", ".icns"],
    "Documents": [".doc", ".docx", ".dot", ".dotx", ".dotm", ".xls", ".xlsx", ".xlsm", ".xlsb", ".xlt", ".xltx", ".xltm", ".ppt", ".pptx", ".pot", ".potx", ".potm", ".pptm", ".pdf", ".txt", ".rtf", ".odt", ".ods", ".odp", ".csv", ".md", ".tex"],
    "Videos": [".mp4", ".mov", ".m4v", ".mkv", ".avi", ".wmv", ".flv", ".webm", ".mpeg", ".mpg", ".mp2", ".mpe", ".mpv", ".m2v", ".m4v", ".3gp", ".3g2"],
    "Music": [".mp3", ".aac", ".m4a", ".wav", ".flac", ".alac", ".aiff", ".ogg", ".wma", ".ac3", ".amr", ".ra", ".mid", ".midi", ".opus", ".spx", ".opus"],
    "Archives": [".zip", ".rar", ".tar", ".tar.gz", ".tgz", ".tar.bz2", ".tbz2", ".tar.xz", ".txz", ".7z", ".sit", ".sitx"],
    "Programs": [".exe", ".msi", ".dmg", ".app", ".deb", ".rpm"],
    "Scripts": [".py", ".ipynb", ".sh", ".bash", ".zsh", ".fish", ".bat", ".cmd", ".ps1", ".vbs", ".js", ".rb", ".php", ".pl", ".lua", ".scala", ".go", ".dart", ".cs", ".java", ".m", ".r", ".swift", ".ts", ".coffee", ".html", ".css"],
    "Spreadsheets": [".xlsx", ".xlsm", ".xlsb", ".xltx", ".xltm", ".ods", ".csv", ".tsv"],
    "Presentations": [".pptx", ".pptm", ".potx", ".potm", ".ppsx", ".ppsm"],
    "Web": [".html", ".htm", ".css", ".js", ".php", ".asp", ".aspx", ".jsp", ".xml"],
    "Other": []
}

# Create a new folder for each category
for category in categories:
    category_path = os.path.join(documents_path, category)
    if not os.path.exists(category_path):
        os.mkdir(category_path)

# Loop through the files in the documents folder
for filename in os.listdir(documents_path):
    file_path = os.path.join(documents_path, filename)
    if os.path.isfile(file_path):
        # Determine the file type based on its extension
        file_extension = os.path.splitext(filename)[1].lower()
        file_category = "Other"  # default category if file type is unknown
        for category, extensions in categories.items():
            if file_extension in extensions:
                file_category = category
                break

        # Copy the file to the appropriate category folder
        category_path = os.path.join(documents_path, file_category)
        shutil.move(file_path, category_path)
