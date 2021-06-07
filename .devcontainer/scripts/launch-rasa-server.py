
import os
import re
import subprocess
import sys

from rasa.__main__ import main

if __name__ == '__main__':
    dir = os.path.dirname(os.path.abspath(__file__))

    print("Starting ngrok")
    subprocess.call(os.path.join(dir, "./start-ngrok.sh"))
    
    print("Updating credentials.yml")
    subprocess.call(os.path.join(dir, "./update-credentials.sh"))
    
    print("Training model")
    subprocess.call(os.path.join(dir, "./train-model.sh"))
    
    print("Launching rasa")
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
