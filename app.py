from flask import Flask, render_template, request, jsonify
from algorithm.tradingbot import run
from datetime import datetime
from flask_executor import Executor
import os, glob

app = Flask(__name__)
executor = Executor(app)

@app.route('/')
def hello_world():
    return render_template('index.html')

def long_running_task(start_date, end_date):
    run(start_date, end_date)

    # Get a list of all .html files in the 'algorithm/logs' directory
    files = glob.glob('logs/*.html')

    # Sort the files by modification time
    files.sort(key=os.path.getmtime, reverse=True)

    # Get the two most recently modified files
    recent_file1 = files[0] if len(files) > 0 else 'default.html'
    recent_file2 = files[1] if len(files) > 1 else 'default.html'

    # Move the files to the static directory and get the new file paths
    if recent_file1 != 'default.html':
        os.rename(recent_file1, 'static/' + os.path.basename(recent_file1))
        recent_file1 = os.path.basename(recent_file1)

    if recent_file2 != 'default.html':
        os.rename(recent_file2, 'static/' + os.path.basename(recent_file2))
        recent_file2 = os.path.basename(recent_file2)

    return {'file1': recent_file1, 'file2': recent_file2}

@app.route('/start-task', methods=['POST'])
def start_task():
    start_date = request.json.get('start_date')
    end_date = request.json.get('end_date')
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    future = executor.submit(long_running_task, start_date, end_date)
    return jsonify({"message": "Task started", "task_id": id(future)})

@app.route('/task-status/<int:task_id>', methods=['GET'])
def task_status(task_id):
    future = executor.futures._futures.get(task_id)
    if future is None:
        return jsonify({"message": "Task not found"}), 404
    if future.done():
        return jsonify(future.result())
    return jsonify({"message": "Task is still running"}), 202

@app.route('/backtrade/<start_date>/<end_date>', methods=['GET'])
def backtrade(start_date, end_date):
    start_date = datetime.strptime(str(start_date), "%Y-%m-%d")
    end_date = datetime.strptime(str(end_date), "%Y-%m-%d")

    run(start_date, end_date)

    # Get a list of all .html files in the 'algorithm/logs' directory
    files = glob.glob('logs/*.html')

    # Sort the files by modification time
    files.sort(key=os.path.getmtime, reverse=True)

    # Get the two most recently modified files
    recent_file1 = files[0] if len(files) > 0 else 'default.html'
    recent_file2 = files[1] if len(files) > 1 else 'default.html'

    # Move the files to the static directory and get the new file paths
    if recent_file1 != 'default.html':
        os.rename(recent_file1, 'static/' + os.path.basename(recent_file1))
        recent_file1 = os.path.basename(recent_file1)

    if recent_file2 != 'default.html':
        os.rename(recent_file2, 'static/' + os.path.basename(recent_file2))
        recent_file2 = os.path.basename(recent_file2)

    return render_template('backtrade.html', file1=recent_file1, file2=recent_file2)

if __name__ == '__main__':
    app.run(threaded=False)
