import ansible_runner
from config import data_dir


def run_playbook(playbook, extravars):
    """
    Method to run ansible playbook
    """
    result = ('Playbook not executed', 1)
    try:
        r = ansible_runner.run(
            private_data_dir=data_dir,
            playbook=playbook,
            extravars=extravars
        )
        result = (r.status, r.rc)
    except Exception as e:
        result = ('failed to run playbook: %s' % str(e), 1)
    finally:
        return result
