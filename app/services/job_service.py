from app.models.job import Job

class JobService:
    def __init__(self):
        self.jobs = []

    def create_job(self, title, description, company, location, salary):
        job = Job(title, description, company, location, salary)
        self.jobs.append(job)
        return job

    def get_all_jobs(self):
        return self.jobs

    def get_job_by_id(self, job_id):
        return next((job for job in self.jobs if job.id == job_id), None)

    def update_job(self, job_id, data):
        job = self.get_job_by_id(job_id)
        if job:
            job.title = data.get("title", job.title)
            job.description = data.get("description", job.description)
            job.company = data.get("company", job.company)
            job.location = data.get("location", job.location)
            job.salary = data.get("salary", job.salary)
        return job

    def delete_job(self, job_id):
        job = self.get_job_by_id(job_id)
        if job:
            self.jobs.remove(job)
        return job
