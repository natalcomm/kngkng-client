import threading, time, requests, os

username = input(">Username: ")


no_input = True

def cls():
        os.system('cls' if os.name=='nt' else 'clear')

def add_up_time():
    checkmsg = "False"
    while no_input:
        time.sleep(0.5)
        get = requests.get('https://chat.5x.repl.co/log.txt')
        
        cmsg = str(get.text)
        #.split('\n')
        if cmsg != checkmsg:
            t = time.localtime()
            print("-------------------------------")
            current_time = time.strftime("Last update: ""%H:%M:%S", t)
            print(current_time)
            print(cmsg)
            checkmsg = cmsg

    content = input(">Message: ")

    payload = {'content': content, 'username': username}
    requests.get('https://chat.5x.repl.co/post_chat.php', params=payload )


# designed to be called as a thread
def signal_user_input():
    global no_input
    print("-------------------------------")
    i = input(">Hit Enter to send message.\n")
    no_input = False
    # thread exits here


# we're just going to wait for user input while adding up time once...
while 1:
        checkmsg = "False"
        threading.Thread(target = signal_user_input).start()
        no_input = True
        add_up_time()
        

        

        # now, to clear the screen
        cls()

        print(">Message sent.")
