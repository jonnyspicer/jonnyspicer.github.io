from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import datetime
import subprocess

PIPE = subprocess.PIPE
now = datetime.datetime.now()
commitMessage = 'dp' + now.strftime('%y%m%d')

pull = subprocess.Popen(["git", "pull"], stdout=PIPE, stderr=PIPE)
stdoutput, stderroutput = pull.communicate()

if b'fatal' in stdoutput:
    print("Fatal error in pull, aborting script")
    sys.exit()
else:
    print("Pull successful")

add = subprocess.Popen(["git", "add", "-A"])
stdoutput, stderroutput = add.communicate()

commit = subprocess.Popen(["git", "commit", "-m", commitMessage])
stdoutput, stderroutput = commit.communicate()

if b'fatal' in stdoutput:
    print("Fatal error in commit, aborting script")
    sys.exit()
else:
    print("Commit successful")

push = subprocess.Popen(["git", "push"], stdout=PIPE, stderr=PIPE)
stdoutput, stderroutput = push.communicate()

if b'fatal' in stdoutput:
    print("Fatal error in push, aborting script")
    sys.exit()
else:
    print("Push successful")


