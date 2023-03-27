**A simple glitch web server — web server that doesn't work well.**

The script binds to the port `8765` and listens to all incoming http connections.
Whatever path is called, the server will answer with `200OK` text and `200 OK` Status Code, except 5% of requests will get a response with `500` error, 5% of requests – `404` error, and 10% of `200OK` responses will be delayed for 2 seconds.

Use it for educational purposes to show a sequence of requests with errors, e.g. for load testing and reports building.

No usage parameters — change whatever is needed in the script itself.

Install requirements from `requirements.txt` and run with
`python main.py`