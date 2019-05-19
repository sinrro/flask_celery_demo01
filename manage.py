from flask_script import Manager, Server, Shell

from app import create_app

app = create_app('default')


def make_shell_context():
    return dict(app=app)


manager = Manager(app)
manager.add_command('runserver', Server(host='192.168.17.128', port=80, use_debugger=True, use_reloader=True))
manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run(default_command='runserver')
    # manager.run(default_command='shell')
