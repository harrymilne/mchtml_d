import socket
import jinja as jin
from mcstatus.minecraft_query import MinecraftQuery

class StatusWidget:
    def __init__(self, address, port, name):
        self.address = address
        self.port = port
        self.name = name

        j_env = jin.Environment(loader=jin.FileSystemLoader("templates/"))
        self.widget_t = j_env.get_template("widget.html")

    def refresh_data(self):
        query = MinecraftQuery(self.address, self.port)
        try:
            self.server_info = query.get_rules()
            self.response = "ONLINE"
        except socket.timeout:
            self.response = "OFFLINE"
        print("SERVER: " + self.response)

    def gen_html(self):
        self.html = self.widget_t.render(
            server_name = self.name,
            server_status = self.response,
            num_players = "/".join([
                str(self.server_info["numplayers"]), 
                str(self.server_info["maxplayers"])]),
            players = self.server_info["players"]
        )

    def write_out(self, fname):
        with open(fname, "w") as f:
            f.write(self.html)
        print("HTML WRITTEN TO {}".format(fname))
