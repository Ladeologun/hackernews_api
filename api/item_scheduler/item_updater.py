from apscheduler.schedulers.background import BackgroundScheduler
from api.view.read_view import StoryViewset

def start():
    scheduler = BackgroundScheduler()
    story = StoryViewset()
    scheduler.add_job(story.save_items_data, "interval", minutes=1,id="story_001",replace_existing=True)
    scheduler.start()