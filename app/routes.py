from app import app
import redis
from datetime import datetime
from .config import password
r = redis.StrictRedis(host="104.131.43.222", password=password, decode_responses=True)


def filterprofanity(stringtocheck) -> (bool):
    stringtochecklist = stringtocheck.split()
    print(stringtochecklist)
    templist = []
    with open('profanity.txt') as f:
        for line in f:
            templist.append(line.split('\n')[0].strip("\'"))
    # print(templist)
    for val in templist:
        if val in stringtochecklist:
            print("fouind")
            return False
    return True
    



@app.route('/api/')
@app.route('/index')
def index():
    return "Welcome to nonhumanworks.com! Simply pass in the phrase (even including spaces) you want to use in the url itself, for example <a href='https://nonhumanworks.com/api/dogs%20playing%20golf'>https://nonhumanworks.com/api/dogs in space</a>"


@app.route('/api/<id>') 
def landing_page(id):
    safe = filterprofanity(id)
    if safe:
        print(f"What I received was {id}. Adding to queue.")
        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y-%H-%M-%S")
        r.sadd("prompts", f"{dt_string}-{id}")
        # runner.do_run(id)
        return f"<!DOCTYPE html><body style='font-family:monospace;'><h4>What was received was the following prompt: {id}</ h4><h4>Added to queue. The image will be available at <a href='https://nonhumanworks.com/static/{dt_string}-{id}.png'>https://nonhumanworks.com/static/{dt_string}-{id}.png</a>. Estimated time 5 minutes. The queue is polled every minute and is randomly selected. </h4><h4>See QueueList <a href='https://nonhumanworks.com/api/queuelist'>here</a></h4><h4>See what is currently being worked on: <a href='https://nonhumanworks.com/api/current'>https://nonhumanworks.com/api/current</a></h4></body></html>"
    else:
        return f"<!DOCTYPE html><body style='font-family:monospace;'><h4>You hit the profanity filter. What you typed in is NSFW. Please try again. <a href='https://nonhumanworks.com/api/'>back to api</a></h4>"


@app.route('/api/queuecount')
def queue_count():
    totalqueue = r.scard("prompts")
    return f"<!DOCTYPE html><body style='font-family:monospace;'><h4>Queue to process: {totalqueue}</h4>"


@app.route('/api/queuelist')
def queue_list():
    listmembers = r.smembers("prompts")
    if len(listmembers) < 1:
        listmembers = ["None"]
    fixedlist = [x + "<br>" for x in listmembers]
    fixedstring = "".join(fixedlist)
    current = r.get("current")
    return f"<!DOCTYPE html><body style='font-family:monospace;'><h4>Queue to process:<br><br> {fixedstring}</h4><h4>Currently working on: <a target='_blank' href='https://nonhumanworks.com/api/current'>{current}</a></h4></body>"


@app.route('/api/current')
def get_current():
    listmembers = r.smembers("prompts")
    if len(listmembers) < 1:
        listmembers = ["None"]
    fixedlist = [x + "<br>" for x in listmembers]
    fixedstring = "".join(fixedlist)
    currentwork = r.get("current")
    return f"<!DOCTYPE html><body style='font-family:monospace;'><h4>Currently working on: <a href='https://nonhuman.works/static/{currentwork}.png'>{currentwork}</a> (It will not be available until approx. 5 minutes after start. A watched bot never boils.)</h4><h4><a target='_blank' href='https://nonhumanworks.com/api/queuelist'>Queue</a> to process:<br><br> {fixedstring}</h4><h4>View the current <a href='https://nonhumanworks.com/gallery.php'>gallery</a>.</h4>"
