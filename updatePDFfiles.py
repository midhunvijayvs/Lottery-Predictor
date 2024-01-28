import os
import requests
import ssl
from urllib3 import poolmanager
import tkinter as tk
import time


class TLSAdapter(requests.adapters.HTTPAdapter):

    def init_poolmanager(self, connections, maxsize, block=False):
        """Create and initialize the urllib3 PoolManager."""
        ctx = ssl.create_default_context()
        ctx.set_ciphers('DEFAULT@SECLEVEL=1')
        self.poolmanager = poolmanager.PoolManager(
                num_pools=connections,
                maxsize=maxsize,
                block=block,
                ssl_version=ssl.PROTOCOL_TLS,
                ssl_context=ctx)
def handleUpdatePDFFiles(draw_serial_from, log_area):
    # Delete existing PDF files
    for i in range(1, 8):
        file_path = f"{i}.pdf"
        if os.path.exists(file_path):
            os.remove(file_path)

    # Fetch and save new PDF files
    base_url = "https://result.keralalotteries.com/viewlotisresult.php?drawserial="

    session = requests.session()
    session.mount('https://', TLSAdapter())

    for draw_serial in range(draw_serial_from, draw_serial_from + 7):
        url = base_url + str(draw_serial)

        time.sleep(0.1)  # Add a small delay between log updates
        log_area.update()  # Update the text widget to show the new log
        log_area.insert(tk.END, f"Downloading {draw_serial}.pdf...\n")

        res = session.get(url)
        with open(str(draw_serial - draw_serial_from + 1) + ".pdf", "wb") as f:
            f.write(res.content)
            log_area.insert(tk.END, f"{draw_serial}.pdf downloaded.\n")



    log_area.insert(tk.END, "PDF files updated successfully!\n")
