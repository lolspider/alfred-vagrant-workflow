from subprocess import call


def external_trigger(name, argument):
    """
    Call to external trigger in Alfred
    """
    call(['/usr/bin/osascript', '-e',
          'tell application "Alfred 2" to run trigger "{0}" '
          'in workflow "com.sverdlik.michael" '
          'with argument "{1}"'.format(name, argument)])


def send_notification(msg):
    """
    Trigger notification with msg as content
    """
    external_trigger('send_notification', msg)


def open_terminal(path):
    """
    Trigger opening terminal and cd to path
    """
    external_trigger('open_dir', path)


def run_vagrant(arg):
    """
    Trigger running Vagrant in terminal
    """
    external_trigger('run_vagrant', arg)


def run_alfred(action):
    """
    Launch Alfred 2 via AppleScript and search for 'action'
    """
    call(['/usr/bin/osascript', '-e',
          'tell application "Alfred 2" to search "{0}"'.format(action)])
