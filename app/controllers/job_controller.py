from flask import Blueprint, request, jsonify
from app.services.job_service import JobService

job_blueprint = Blueprint("jobs", __name__, url_prefix="/jobs")
job_service = JobService()

@job_blueprint.route("/", methods=["POST"])
def create_job():
    data = request.json
    job = job_service.create_job(
        title=data["title"],
        description=data["description"],
        company=data["company"],
        location=data["location"],
        salary=data["salary"]
    )
    return jsonify(job.to_dict()), 201

@job_blueprint.route("/", methods=["GET"])
def get_jobs():
    jobs = job_service.get_all_jobs()
    return jsonify([job.to_dict() for job in jobs])

@job_blueprint.route("/<int:job_id>", methods=["GET"])
def get_job(job_id):
    job = job_service.get_job_by_id(job_id)
    if job:
        return jsonify(job.to_dict())
    return jsonify({"error": "Job not found"}), 404

@job_blueprint.route("/<int:job_id>", methods=["PUT"])
def update_job(job_id):
    data = request.json
    job = job_service.update_job(job_id, data)
    if job:
        return jsonify(job.to_dict())
    return jsonify({"error": "Job not found"}), 404

@job_blueprint.route("/<int:job_id>", methods=["DELETE"])
def delete_job(job_id):
    job = job_service.delete_job(job_id)
    if job:
        return jsonify({"message": "Job deleted successfully"})
    return jsonify({"error": "Job not found"}), 404
