import os
from app import app
if __name__ == 'main':
  port = int(os.environ.get("PORT",4000))
  app.run(host="0.0.0.0", port = port)
