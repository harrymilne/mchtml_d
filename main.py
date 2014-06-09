import time
from ConfigParser import ConfigParser
from status_widget import StatusWidget

def main(s_widget):
    while True:
        s_widget.refresh_data()
        s_widget.gen_html()
        s_widget.write_out(TARGET_FILE)
        time.sleep(30)

if __name__ == "__main__":
    cfg = ConfigParser()
    cfg.read("server.cfg")
    SERVER_IP = cfg.get("server", "ip")
    SERVER_PORT = cfg.getint("server", "port")
    SERVER_NAME = cfg.get("server", "name")
    TARGET_FILE = cfg.get("out", "file")

    s_widget = StatusWidget(
    SERVER_IP, 
    SERVER_PORT, 
    SERVER_NAME
    )

    main(s_widget)