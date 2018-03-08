# encoding: utf-8
# run.py

from app import interact
from app import session
from app import task


if __name__ == "__main__":
    session.setup(interact.get_session_info())
    task.setup(session)
    task.run(session)
