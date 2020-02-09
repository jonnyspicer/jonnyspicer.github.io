from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import datetime
import pyautogui
import subprocess

pyautogui.moveTo(1000, 2000)
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

commit = subprocess.Popen(["git", "commit", "-m", commitMessage], shell=True, stdout=PIPE, stderr=PIPE)
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

print("Waiting for Github Pages to build...")

time.sleep(30)

def LastPostDate():
    frontpage = urlopen('https://jonnyspicer.com').read()
    parsed_frontpage = BeautifulSoup(frontpage, 'html.parser')
    date_span = parsed_frontpage.body.find(
        'div', class_='recent-posts-mendokusai').find('span').text
    date_today = now.strftime("%d %b %Y")
    return date_today in date_span

print("Checking whether new post is on live site")
print("First try...")
if LastPostDate() == True:
    print("Post published!")
else:
    time.sleep(30)
    print("Second try...")
    if LastPostDate() == True:
        print("Post published!")
    else:
        time.sleep(30)
        print("Third try...")
        if LastPostDate() == True:
            print("Post published!")
        else:
            print("Something went wrong. If only you'd written an actual unit test with exceptions!")


