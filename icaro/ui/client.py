import socket
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog


HOST = '127.0.0.1'
PORT = 9999



class Client:

    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

        msg = tkinter.Tk() # janela
        msg.withdraw()

        self.nickname = simpledialog.askstring("Nickname", "Please choose a nickname", parent=msg)

        self.gui_done = False

        self.running = True

        gui_thread = threading.Thread(target=self.gui_loop)
        gui_thread.start()

        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

    def gui_loop(self):
        self.win = tkinter.Tk()
        self.win.config(bg="lightgray")

        self.chat_label = tkinter.Label(self.win, text="Chat:", bg="lightgray")
        self.chat_label.config(font=("Arial", 12))
        self.chat_label.pack(padx=20, pady=5)

        self.text_area = tkinter.scrolledtext.ScrolledText(self.win)
        self.text_area.pack(padx=20, pady=5)
        self.text_area.config(state="disabled")

        self.msg_label = tkinter.Label(self.win, text="Message:", bg="lightgray")
        self.msg_label.config(font=("Arial", 12))
        self.msg_label.pack(padx=20, pady=5)

        self.input_area = tkinter.Text(self.win, height=3)
        self.input_area.pack(padx=20, pady=5)

        self.send_button = tkinter.Button(self.win, text="Send", command=self.write)
        self.send_button.config(font=("Arial", 12))
        self.send_button.pack(padx=20, pady=5)

        self.gui_done = True
        self.win.mainloop()
        self.win.protocol("WN_DELETE_WINDOW", self.stop)





    def write(self):
        msg = f'{self.nickname}: {self.input_area.get('1.0', 'end')}'
        self.sock.send(msg.encode('utf-8'))
        self.input_area.delete('1.0', 'end')




    def stop(self):
        self.running = False
        self.win.destroy()
        self.sock.close()
        exit(0)




    def receive(self):
        while self.running:
            try:
                msg = self.sock.recv(1024)
                if msg == 'NICK':
                    self.sock.send(self.nickname.encode('utf-8'))
                else:
                    if self.gui_done:
                        self.text_area.config(state='normal')
                        self.text_area.insert('end', msg)
                        self.text_area.yview('end')
                        self.text_area.config(state="disabled")
            except ConnectionAbortedError:
                break
            except:
                print("Error")
                self.sock.close()
                break

client = Client(HOST, PORT)









nickname = input('Choose a nickname: ')


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))


def receive():
    while True:
        try:
            msg = client.recv(1024).decode('ascii')
            if msg == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(msg)
        except:
            print("Ocorreu um erro")
            client.close()
            break

def write():
    while True:
        try:
            msg = f"{nickname}: {input("")}"
            client.send(msg.encode('ascii'))
        except:
            print("Ocorreu um erro")
            client.close()
            break




'''Agora precisamos atribuir um thread pra cara uma dessas funções para que elas possam rodar ao mesmo tempo'''

receive_thread = threading.Thread(target=receive)
receive_thread.start()


write_thread = threading.Thread(target=write)
write_thread.start()