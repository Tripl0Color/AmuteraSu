#Use on py flask
print ("""$$$$$$$$\        $$\           $$\        $$$$$$\            $$\                     
\__$$  __|       \__|          $$ |      $$  __$$\           $$ |                    
   $$ | $$$$$$\  $$\  $$$$$$\  $$ |      $$ /  \__| $$$$$$\  $$ | $$$$$$\   $$$$$$\  
   $$ |$$  __$$\ $$ |$$  __$$\ $$ |      $$ |      $$  __$$\ $$ |$$  __$$\ $$  __$$\ 
   $$ |$$ |  \__|$$ |$$ /  $$ |$$ |      $$ |      $$ /  $$ |$$ |$$ /  $$ |$$ |  \__|
   $$ |$$ |      $$ |$$ |  $$ |$$ |      $$ |  $$\ $$ |  $$ |$$ |$$ |  $$ |$$ |      
   $$ |$$ |      $$ |$$$$$$$  |$$ |      \$$$$$$  |\$$$$$$  |$$ |\$$$$$$  |$$ |      
   \__|\__|      \__|$$  ____/ \__|$$$$$$\\______/  \______/ \__| \______/ \__|      
                     $$ |          \______|                                          
                     $$ |                                                            
                     \__|    """)
from flask import Flask, request, json
import time
import vk_api
import random
 
vk = vk_api.VkApi(token="paste your token vk group here")        #vk group token here
msg = "msg here"                                                 #Your ded message
app = Flask(__name__)
 
@app.route('/', methods = ["POST"])
def main():
    data = json.loads(request.data)
    if data["type"] == "confirmation":
        return "paste code vk here"                               #code vk here
    elif data["type"] == "message_new":
        object = data["object"]
        id = object["peer_id"]
        body = object["text"]
        if body.lower() == "hello":
                vk.method("messages.send", {"peer_id": id, "message": "hi", "random_id": random.randint(1, 2147483647)})
        
        else:
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})
            vk.method("messages.send", {"peer_id": id, "message": msg, "random_id": random.randint(1, 2147483647)})

    return "ok"

                     
