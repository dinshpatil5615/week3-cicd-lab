from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Week 3 CI/CD pipeline works!",
        "version": "2.0.0",
        "deployed_by": "GitHub Actions + ECR + ECS",
        "new_feature": "auto-deployed v2 without touching AWS console"
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "version": "2.0.0"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)