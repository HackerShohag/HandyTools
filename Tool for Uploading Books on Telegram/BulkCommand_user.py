'''
A tool to upload all the books to a specific telegram group in a specific manner so that everybody can get them on demand. 
Feel free to use all the tools on this repo. These are not copyrighted and pobably will have a free license on the main directory.
'''



from telethon.sync import TelegramClient, events
from os import listdir
from os.path import isfile, join
from dotenv import load_dotenv
import os

def send_files(book_type, filename, file_index):
    caption = f'/filter "/books {book_type} {file_index}" \n#Warning: Please, don\'t share with anyone.'
    return_obj = client.send_file(chat_id, filename, caption=caption)
    if return_obj.to_dict()["message"] == caption:
        print(f"Successfully uploaded file {filename} with index {file_index}")
        return_obj.delete()
    #needs to implement deleting the replies.

def read_files(path):
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    onlyfiles.sort()
    with open("java_list","a") as file:
        for filename in onlyfiles:
            file.write(f"{onlyfiles.index(filename) + 1}. {filename.replace('_', ' ').replace('.pdf', '')}\n")
    return onlyfiles

if __name__ == "__main__":
    load_dotenv()

    api_id = os.getenv("API_ID")
    api_hash = os.getenv("API_HASH")
    phone = os.getenv("PHONE")
    chat_id = int(os.getenv("CHAT_ID"))
    path = '/home/shohag/Documents/pdfs/java/'

    files = read_files(path)     

    client = TelegramClient('name', api_id, api_hash)
    client.connect()
    for filename in files:
        file_index = files.index(filename) + 1;
        send_files("java", path + filename, file_index)


    client.disconnect()
