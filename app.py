from flask import Flask, render_template, request
from algorithm.tradingbot import run
from datetime import datetime
from multiprocessing import Process, Queue
import os,glob

app = Flask(__name__)


def run_backtest(start_date, end_date, queue):
    try:
        run(start_date, end_date)
        queue.put("Backtest completed successfully.")
    except Exception as e:
        queue.put((str(e), None, None))


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/backtrade/<start_date>/<end_date>', methods=['GET'])
def backtrade(start_date, end_date):
    start_date = datetime.strptime(str(start_date), "%Y-%m-%d")
    end_date = datetime.strptime(str(end_date), "%Y-%m-%d")

    queue = Queue()
    log_queue = Queue()
    p = Process(target=run_backtest, args=(start_date, end_date, queue))
    p.start()

    p.join()


    # Get a list of all .html files in the 'algorithm/logs' directory
    files = glob.glob('logs/*.html')

    # Sort the files by modification time
    files.sort(key=os.path.getmtime, reverse=True)

    # Get the two most recently modified files
    recent_file1 = files[0] if len(files) > 0 else None
    recent_file2 = files[1] if len(files) > 1 else None

    # Move the files to the static directory and get the new file paths
    if recent_file1:
        os.rename(recent_file1, 'static/' + os.path.basename(recent_file1))
        recent_file1 = os.path.basename(recent_file1)

    if recent_file2:
        os.rename(recent_file2, 'static/' + os.path.basename(recent_file2))
        recent_file2 = os.path.basename(recent_file2)

    return render_template('backtrade.html', file1=recent_file1, file2=recent_file2)


if __name__ == '__main__':
    app.run(threaded=False)
