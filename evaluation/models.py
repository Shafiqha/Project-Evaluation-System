from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    guide_name = models.CharField(max_length=100, blank=True, null=True)
    github_repo = models.URLField(blank=True, null=True)
    ppt_file = models.FileField(upload_to='ppt_files/', blank=True, null=True)
    average_marks = models.FloatField(default=0)

    # Files for different phases
    phase1_file = models.FileField(upload_to='phase1_files/', blank=True, null=True)
    phase2_file = models.FileField(upload_to='phase2_files/', blank=True, null=True)
    phase3_file = models.FileField(upload_to='phase3_files/', blank=True, null=True)

    students = models.ManyToManyField(Student, related_name='teams')

    def _str_(self):
        return self.name

class Evaluation(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='evaluations')
    panelist_name = models.CharField(max_length=100, null=True)
    phase = models.CharField(
        max_length=10, 
        choices=[('phase1', 'Phase 1'), ('phase2', 'Phase 2'), ('phase3', 'Phase 3')],
        default='phase1'  # Set default phase value
    )
    

    # Rubric fields
    abstract_synopsis = models.IntegerField(default=0)
    topic_relevance = models.IntegerField(default=0)
    problem_identification = models.IntegerField(default=0)
    objectives_methodology = models.IntegerField(default=0)
    literature_survey = models.IntegerField(default=0)
    documentation = models.IntegerField(default=0)
    results = models.IntegerField(default=0)
    presentation_quality = models.IntegerField(default=0)
    communication_skills = models.IntegerField(default=0)
    technical_knowledge = models.IntegerField(default=0)
    individual_involvement = models.IntegerField(default=0)
    fundamentals_questions = models.IntegerField(default=0)
    clarity_in_answers = models.IntegerField(default=0)
    understanding_ability = models.IntegerField(default=0)
    attitude_towards_questions = models.IntegerField(default=0)

    def calculate_total_marks(self):
        total_marks = (
            self.abstract_synopsis + self.topic_relevance + self.problem_identification +
            self.objectives_methodology + self.literature_survey + self.documentation +
            self.results + self.presentation_quality + self.communication_skills +
            self.technical_knowledge + self.individual_involvement +
            self.fundamentals_questions + self.clarity_in_answers +
            self.understanding_ability + self.attitude_towards_questions
        )
        return total_marks   # Number of rubrics
    def calculate_average(self):
        # Calculate the average marks of all rubric fields
        total_marks = self.calculate_total_marks()
        number_of_fields = 14  # The total number of rubric fields
        return total_marks / number_of_fields

    def _str_(self):
        return f"Evaluation for {self.team.name} by {self.panelist_name} for {self.phase}"

