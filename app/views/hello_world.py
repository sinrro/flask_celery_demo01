from . import view
from app.tasks import add_together,add_together1


@view.route('/', methods=['GET', 'POST'])
def index():
    result = add_together1.delay(23, 42)
    print("task_id:{}".format(result))
    return "add_together is running...."
