class Job:
    _id_counter = 1

    def __init__(self, title, description, company, location, salary):
        self.id = Job._id_counter
        Job._id_counter += 1
        self.title = title
        self.description = description
        self.company = company
        self.location = location
        self.salary = salary

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "company": self.company,
            "location": self.location,
            "salary": self.salary
        }
