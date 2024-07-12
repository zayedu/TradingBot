from flask import Flask, render_template, request
from algorithm.tradingbot import run
from datetime import datetime
from multiprocessing import Process, Queue

app = Flask(__name__)

def run_backtest(start_date, end_date, queue):
    try:
        results, strategy = run(start_date, end_date)
        queue.put("Backtest completed successfully.")
    except Exception as e:
        queue.put(str(e))

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/backtrade/<start_date>/<end_date>', methods=['GET'])
def backtrade(start_date, end_date):
    start_date = datetime.strptime(str(start_date), "%Y-%m-%d")
    end_date = datetime.strptime(str(end_date), "%Y-%m-%d")

    queue = Queue()
    p = Process(target=run_backtest, args=(start_date, end_date, queue))
    p.start()
    p.join()

    result = queue.get()

    return render_template('backtrade.html', result=result)

if __name__ == '__main__':
    app.run(threaded=False)
