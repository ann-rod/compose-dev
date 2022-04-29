"""Initialize Flask app."""
from flask import Flask
from flask_assets import Environment, Bundle
import sys
import app.options


ipa = sys.argv[1]
app.options.options.sethost(ipa)


# # setup reverse proxy if on kubernetes
try: proxy = sys.argv[2]
except:
    pass
else:
    app.options.options.setproxy(proxy)

import logging
logger = logging.getLogger('root')

from app import init_app
"""Application entry point."""
if __name__ == "__main__":
    app = init_app()
    port = 5026
    app.run(host="0.0.0.0", debug=False,port=port)
