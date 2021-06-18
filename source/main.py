import threading, time, requests

username = input(">Username: ")


no_input = True

def add_up_time():
    checkmsg = ""
    while no_input:
        time.sleep(0.5)
        get = requests.get('https://#####API_LOGS#####')
        
        cmsg = str(get.text)
        if cmsg != checkmsg:
            t = time.localtime()
            print("-------------------------------")
            current_time = time.strftime("Last update: ""%H:%M:%S", t)
            print(current_time)
            print(checkmsg)
            checkmsg = cmsg

    content = input(">Message: ")

    payload = {'content': content, 'username': username}
    r = requests.get('https://#####API_SEND#####', params=payload )



def signal_user_input():
    global no_input
    print("-------------------------------")
    i = input(">Hit Enter to send message.\n")
    no_input = False
    
    
while 1:

        threading.Thread(target = signal_user_input).start()
        no_input = True
        add_up_time()

        print(">Message sent.")
