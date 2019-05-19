from . import view
from app import add_together


@view.route('/', methods=['GET', 'POST'])
def index():
    result = add_together.delay(23, 42)
    print("task_id:{}".format(result))
    return "add_together is running...."
