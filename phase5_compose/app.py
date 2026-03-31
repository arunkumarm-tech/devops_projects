import time
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis-db', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return f"<h1>Devops Master Arun!</h1><p>This multi-container app has been viewed {count} times.</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
