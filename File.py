from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os 
import json
import shutil
from datetime import datetime
from time import gmtime, strftime

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != 'Soumen':
                # try:
                    new_name = filename
                    extension = 'noname'
                    try:
                        extension = str(os.path.splitext(folder_to_track + '/' + filename)[1])
                        path = extensions_folders[extension]
                    except Exception:
                        extension = 'noname'

                    now = datetime.now()
                    year = now.strftime("%Y")
                    month = now.strftime("%m")

                    folder_destination_path = extensions_folders[extension]
                    
                    year_exists = False
                    month_exists = False
                    for folder_name in os.listdir(extensions_folders[extension]):
                        if folder_name == year:
                            folder_destination_path = extensions_folders[extension] + "/" +year
                            year_exists = True
                            for folder_month in os.listdir(folder_destination_path):
                                if month == folder_month:
                                    folder_destination_path = extensions_folders[extension] + "/" + year + "/" + month
                                    month_exists = True
                    if not year_exists:
                        os.mkdir(extensions_folders[extension] + "/" + year)
                        folder_destination_path = extensions_folders[extension] + "/" + year
                    if not month_exists:
                        os.mkdir(folder_destination_path + "/" + month)
                        folder_destination_path = folder_destination_path + "/" + month


                    file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    while file_exists:
                        i += 1
                        new_name = os.path.splitext(folder_to_track + '/' + filename)[0] + str(i) + os.path.splitext(folder_to_track + '/' + filename)[1]
                        new_name = new_name.split("/")[4]
                        file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    src = folder_to_track + "/" + filename

                    new_name = folder_destination_path + "/" + new_name
                    os.rename(src, new_name)
                # except Exception:
                #     print(filename)
#Common_literal = '/Users/Soumen/Downloads/Downloaded_Category/'
extensions_folders = {
#No name
    'noname' : "/Users/Soumen/Downloads/Downloaded_Category/Other",
#Audio
    '.aif' : "/Users/Soumen/Downloads/Downloaded_Category/Audio",
    '.cda' : "/Users/Soumen/Downloads/Downloaded_Category/Audio",
    '.mid' : "/Users/Soumen/Downloads/Downloaded_Category/Audio",
    '.midi' : "/Users/Soumen/Downloads/Downloaded_Category/Audio",
    '.mp3' : "/Users/Soumen/Downloads/Downloaded_Category/Audio",
    '.mpa' : "/Users/Soumen/Downloads/Downloaded_Category/Audio",
    '.ogg' : "/Users/Soumen/Downloads/Downloaded_Category/Audio",
    '.wav' : "/Users/Soumen/Downloads/Downloaded_Category/Audio",
    '.wma' : "/Users/Soumen/Downloads/Downloaded_Category/Audio",
    '.wpl' : "/Users/Soumen/Downloads/Downloaded_Category/Audio",
    '.m3u' : "/Users/Soumen/Downloads/Downloaded_Category/Audio",
#Text
    '.txt' : "/Users/Soumen/Downloads/Downloaded_Category/Documents",
    '.doc' : "/Users/Soumen/Downloads/Downloaded_Category/Documents/Microsoft_Docs",
    '.docx' : "/Users/Soumen/Downloads/Downloaded_Category/Documents/Microsoft_Docs",
    '.odt ' : "/Users/Soumen/Downloads/Downloaded_Category/Documents",
    '.pdf': "/Users/Soumen/Downloads/Downloaded_Category/Documents",
    '.rtf': "/Users/Soumen/Downloads/Downloaded_Category/Documents",
    '.tex': "/Users/Soumen/Downloads/Downloaded_Category/Documents",
    '.wks ': "/Users/Soumen/Downloads/Downloaded_Category/Documents",
    '.wps': "/Users/Soumen/Downloads/Downloaded_Category/Documents",
    '.wpd': "/Users/Soumen/Downloads/Downloaded_Category/Documents",
#Video
    '.3g2': "/Users/Soumen/Downloads/Downloaded_Category/Video",
    '.3gp': "/Users/Soumen/Downloads/Downloaded_Category/Video",
    '.avi': "/Users/Soumen/Downloads/Downloaded_Category/Video",
    '.flv': "/Users/Soumen/Downloads/Downloaded_Category/Video",
    '.h264': "/Users/Soumen/Downloads/Downloaded_Category/Video",
    '.m4v': "/Users/Soumen/Downloads/Downloaded_Category/Video",
    '.mkv': "/Users/Soumen/Downloads/Downloaded_Category/Video",
    '.mov': "/Users/Soumen/Downloads/Downloaded_Category/Video",
    '.mp4': "/Users/Soumen/Downloads/Downloaded_Category/Video",
    '.mpg': "/Users/Soumen/Downloads/Downloaded_Category/Video",
    '.mpeg': "/Users/Soumen/Downloads/Downloaded_Category/Video",
    '.rm': "/Users/Soumen/Downloads/Downloaded_Category/Video",
    '.swf': "/Users/Soumen/Downloads/Downloaded_Category/Video",
    '.vob': "/Users/Soumen/Downloads/Downloaded_Category/Video",
    '.wmv': "/Users/Soumen/Downloads/Downloaded_Category/Video",
#Images
    '.ai': "/Users/Soumen/Downloads/Downloaded_Category/Images",
    '.bmp': "/Users/Soumen/Downloads/Downloaded_Category/Images",
    '.gif': "/Users/Soumen/Downloads/Downloaded_Category/Images",
    '.ico': "/Users/Soumen/Downloads/Downloaded_Category/Images",
    '.jpg': "/Users/Soumen/Downloads/Downloaded_Category/Images",
    '.jpeg': "/Users/Soumen/Downloads/Downloaded_Category/Images",
    '.png': "/Users/Soumen/Downloads/Downloaded_Category/Images",
    '.ps': "/Users/Soumen/Downloads/Downloaded_Category/Images",
    '.psd': "/Users/Soumen/Downloads/Downloaded_Category/Images",
    '.svg': "/Users/Soumen/Downloads/Downloaded_Category/Images",
    '.tif': "/Users/Soumen/Downloads/Downloaded_Category/Images",
    '.tiff': "/Users/Soumen/Downloads/Downloaded_Category/Images",
    '.CR2': "/Users/Soumen/Downloads/Downloaded_Category/Images",
#Internet
    '.asp': "/Users/Soumen/Downloads/Downloaded_Category/Other/Internet",
    '.aspx': "/Users/Soumen/Downloads/Downloaded_Category/Other/Internet",
    '.cer': "/Users/Soumen/Downloads/Downloaded_Category/Other/Internet",
    '.cfm': "/Users/Soumen/Downloads/Downloaded_Category/Other/Internet",
    '.cgi': "/Users/Soumen/Downloads/Downloaded_Category/Other/Internet",
    '.pl': "/Users/Soumen/Downloads/Downloaded_Category/Other/Internet",
    '.css': "/Users/Soumen/Downloads/Downloaded_Category/Other/Internet",
    '.htm': "/Users/Soumen/Downloads/Downloaded_Category/Other/Internet",
    '.js': "/Users/Soumen/Downloads/Downloaded_Category/Other/Internet",
    '.jsp': "/Users/Soumen/Downloads/Downloaded_Category/Other/Internet",
    '.part': "/Users/Soumen/Downloads/Downloaded_Category/Other/Internet",
    '.php': "/Users/Soumen/Downloads/Downloaded_Category/Other/Internet",
    '.rss': "/Users/Soumen/Downloads/Downloaded_Category/Other/Internet",
    '.xhtml': "/Users/Soumen/Downloads/Downloaded_Category/Other/Internet",
#Compressed
    '.7z': "/Users/Soumen/Downloads/Downloaded_Category/Compressed",
    '.arj': "/Users/Soumen/Downloads/Downloaded_Category/Compressed",
    '.deb': "/Users/Soumen/Downloads/Downloaded_Category/Compressed",
    '.pkg': "/Users/Soumen/Downloads/Downloaded_Category/Compressed",
    '.rar': "/Users/Soumen/Downloads/Downloaded_Category/Compressed",
    '.rpm': "/Users/Soumen/Downloads/Downloaded_Category/Compressed",
    '.tar.gz': "/Users/Soumen/Downloads/Downloaded_Category/Compressed",
    '.z': "/Users/Soumen/Downloads/Downloaded_Category/Compressed",
    '.zip': "/Users/Soumen/Downloads/Downloaded_Category/Compressed",
#Disc
    '.bin': "/Users/Soumen/Other/Disc",
    '.dmg': "/Users/Soumen/Other/Disc",
    '.iso': "/Users/Soumen/Other/Disc",
    '.toast': "/Users/Soumen/Other/Disc",
    '.vcd': "/Users/Soumen/Other/Disc",
#Data
    '.csv': "/Users/Soumen/Programming/Database",
    '.dat': "/Users/Soumen/Programming/Database",
    '.db': "/Users/Soumen/Programming/Database",
    '.dbf': "/Users/Soumen/Programming/Database",
    '.log': "/Users/Soumen/Programming/Database",
    '.mdb': "/Users/Soumen/Programming/Database",
    '.sav': "/Users/Soumen/Programming/Database",
    '.sql': "/Users/Soumen/Programming/Database",
    '.tar': "/Users/Soumen/Programming/Database",
    '.xml': "/Users/Soumen/Programming/Database",
    '.json': "/Users/Soumen/Programming/Database",
#Executables
    '.apk': "/Users/Soumen/Other/Executables",
    '.bat': "/Users/Soumen/Other/Executables",
    '.com': "/Users/Soumen/Other/Executables",
    '.exe': "/Users/Soumen/Other/Executables",
    '.gadget': "/Users/Soumen/Other/Executables",
    '.jar': "/Users/Soumen/Other/Executables",
    '.wsf': "/Users/Soumen/Other/Executables",
#Fonts
    '.fnt': "/Users/Soumen/Other/Fonts",
    '.fon': "/Users/Soumen/Other/Fonts",
    '.otf': "/Users/Soumen/Other/Fonts",
    '.ttf': "/Users/Soumen/Other/Fonts",
#Presentations
    '.key': "/Users/Soumen/Text/Presentations",
    '.odp': "/Users/Soumen/Text/Presentations",
    '.pps': "/Users/Soumen/Text/Presentations",
    '.ppt': "/Users/Soumen/Text/Presentations",
    '.pptx': "/Users/Soumen/Text/Presentations",
#Programming
    '.c': "/Users/Soumen/Programming/C&C++",
    '.class': "/Users/Soumen/Programming/Java",
    '.dart': "/Users/Soumen/Programming/Dart",
    '.py': "/Users/Soumen/Programming/Python",
    '.sh': "/Users/Soumen/Programming/Shell",
    '.swift': "/Users/Soumen/Programming/Swift",
    '.html': "/Users/Soumen/Programming/C&C++",
    '.h': "/Users/Soumen/Programming/C&C++",
#Spreadsheets
    '.ods' : "/Users/Soumen/Downloads/Downloaded_Category/Documents/Microsoft_Docs",
    '.xlr' : "/Users/Soumen/Downloads/Downloaded_Category/Documents/Microsoft_Docs",
    '.xls' : "/Users/Soumen/Downloads/Downloaded_Category/Documents/Microsoft_Docs",
    '.xlsx' : "/Users/Soumen/Downloads/Downloaded_Category/Documents/Microsoft_Docs",
#System
    '.bak' : "/Users/Soumen/Text/Other/System",
    '.cab' : "/Users/Soumen/Text/Other/System",
    '.cfg' : "/Users/Soumen/Text/Other/System",
    '.cpl' : "/Users/Soumen/Text/Other/System",
    '.cur' : "/Users/Soumen/Text/Other/System",
    '.dll' : "/Users/Soumen/Text/Other/System",
    '.dmp' : "/Users/Soumen/Text/Other/System",
    '.drv' : "/Users/Soumen/Text/Other/System",
    '.icns' : "/Users/Soumen/Text/Other/System",
    '.ico' : "/Users/Soumen/Text/Other/System",
    '.ini' : "/Users/Soumen/Text/Other/System",
    '.lnk' : "/Users/Soumen/Text/Other/System",
    '.msi' : "/Users/Soumen/Text/Other/System",
    '.sys' : "/Users/Soumen/Text/Other/System",
    '.tmp' : "/Users/Soumen/Text/Other/System",
}

folder_to_track = 'd/win/Downloads'
folder_destination = '/Users/Soumen/Downloads/Downloaded_Category'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:           
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join() 