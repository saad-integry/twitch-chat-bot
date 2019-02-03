from time import sleep
import socket

class ChatBot:
    HOST = "irc.twitch.tv"
    PORT = 6667
    RATE = (20 / 30)

    def __init__(self, channel_name, auth_token, nick):
        self.channel_name = channel_name
        self.CHAN = f"#{channel_name}"
        self.PASS = f"oauth:{auth_token}"
        self.NICK = nick

    def listen(self):
        try:
            sock = socket.socket()
            sock.connect((self.HOST, self.PORT))
            sock.send("CAP REQ :twitch.tv/tags\r\n".encode("utf-8"))
            sock.send("PASS {}\r\n".format(self.PASS).encode("utf-8"))
            sock.send("NICK {}\r\n".format(self.NICK).encode("utf-8"))
            sock.send("JOIN {}\r\n".format(self.CHAN).encode("utf-8"))
            connected = True
        except Exception as e:
            print(str(e))
            connected = False

        while connected:
            response = sock.recv(1024).decode("utf-8")
            if response == "PING :tmi.twitch.tv\r\n":
                sock.send("PONG :tmi.twitch.tv\r\n".encode())
                print("PONG")
            else:
                if 'bits/' in response:
                    try:
                        display_badge = list(filter(lambda x: 'display-name' in x,
                                                    response.split(':')[0].split(';')))
                        display_name = display_badge[0].split('=')[1]
                        bits_badge = list(filter(lambda x: 'bits' in x,
                                                 response.split(':')[0].split(';')))
                    except Exception as e:
                        print(f'exception message: {str(e)}')
            sleep(1)
