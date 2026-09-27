import os
from flask import Flask, request, jsonify

app = Flask(__name__)

courses_db = {
    101: {"title": "Herramientas de Tecnologías de la Información", "instructor": "Prof. Torres", "enrolled": 35},
    102: {"title": "Fundamentos de Ciberseguridad", "instructor": "Dra. Martínez", "enrolled": 28}
}

@app.route('/')
def home():
    return jsonify({"message": "EduCore Academy Platform API v1.0"})

@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = courses_db.get(course_id)
    if course:
        return jsonify(course), 200
    else:
        return jsonify({"error": "Curso no encontrado"}), 404

if __name__ == '__main__':
    debug_mode = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    host = os.getenv("FLASK_HOST", "127.0.0.1")
    port = int(os.getenv("FLASK_PORT", "5000"))

    app.run(
        debug=debug_mode,
        host=host,
        port=port
    )
