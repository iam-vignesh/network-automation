import socket
import ssl
from datetime import datetime


class Server():
    def __init__(self, name, port, connection):
        self.name = name
        self.port = port
        self.connection = connection.lower()
        self.alert = False

    def check_connection(self):
        msg = ""
        success = False
        now = datetime.now()

        try:
            if self.connection == "plain":
                socket.create_connection((self.name, self.port), timeout=10)
                msg = f"{self.name} is up ON PORT {self.port} with {self.connection}"
                success = True
                self.alert = False
            elif self.connection == "ssl":
                ssl.wrap_socket(socket.create_connection((self.name, self.port), timeout=10))
                msg = f"{self.name} is up ON PORT {self.port} with {self.connection}"
                success = True
                self.alert = False
        except (ConnectionRefusedError, ConnectionResetError) as e:
            msg = f"server: {self.name} {e}"
        except Exception as e:
            msg = f"Sorry! Please check your input: {e}"

        
        if success == False and self.alert == False:
            self.alert = True

        self.result(msg,success,now)

    def result(self, msg, success, now):
        print(msg,"\nSUCCESS:",success,"\nTIMESTAMP:",now)


if __name__ == "__main__":

    instructions = """
+---------------------------------------------------------------------------------------------------------+
* Please enter the server's URL without https:// 
  For eg: google.com, yahoo.com
* The port server uses to accept incming ping should be specified
* Connection type should be specified
+---------------------------------------------------------------------------------------------------------+
"""

    print(instructions)

    while True:


        name = input("Enter the server name: ")
        port = int(input("Enter port number: "))
        connection = input("Enter the connection type (plain/ssl) : ")
        print("\n")
        Server(name,port,connection).check_connection()
        print("+---------------------------------------------------------------------------------------------------------+")