from app.database.models.ProjectModel import Project

class ProjectController:
    @staticmethod
    def add_project(candidate_id, project_name, description=None, start_date=None, end_date=None):
        """
        Add a new project for a candidate.
        """
        project = Project(candidate_id, project_name, description, start_date, end_date)
        return project.save()

    @staticmethod
    def get_projects_by_candidate(candidate_id):
        """
        Retrieve all projects for a specific candidate.
        """
        return Project.find_by_candidate_id(candidate_id)

    @staticmethod
    def delete_project(project_id):
        """
        Delete a project by its ID.
        """
        return Project.delete_by_id(project_id)

    @staticmethod
    def insert_data(project_data):
        """
        Insert project data into the database.
        Args:
            project_data (dict): A dictionary containing project data.
                                 Required fields: candidate_id, project_name.
                                 Optional fields: description, start_date, end_date.
        Returns:
            The inserted project's ID.
        """
        # Validate required fields
        if not project_data.get("candidate_id") or not project_data.get("project_name"):
            raise ValueError("candidate_id and project_name are required fields.")

        # Create a new Project instance and save it
        project = Project(
            candidate_id=project_data["candidate_id"],
            project_name=project_data["project_name"],
            description=project_data.get("description"),  # Optional
            start_date=project_data.get("start_date"),  # Optional
            end_date=project_data.get("end_date")  # Optional
        )
        return project.save()