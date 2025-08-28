from django import forms
from .models import Team, Evaluation

class TeamUploadForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['github_repo', 'ppt_file', 'phase1_file', 'phase2_file', 'phase3_file']

class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = [
            'panelist_name',  # New field
            'phase',  # Field for phase selection
            'abstract_synopsis',
            'topic_relevance',
            'problem_identification',
            'objectives_methodology',
            'literature_survey',
            'documentation',
            'results',
            'presentation_quality',
            'communication_skills',
            'technical_knowledge',
            'individual_involvement',
            'fundamentals_questions',
            'clarity_in_answers',
            'understanding_ability',
            'attitude_towards_questions'
        ]
        widgets = {
            'panelist_name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'phase': forms.Select(choices=[('phase1', 'Phase 1'), ('phase2', 'Phase 2'), ('phase3', 'Phase 3')]),
            'abstract_synopsis': forms.NumberInput(attrs={'min': 0, 'max': 10}),
            'topic_relevance': forms.NumberInput(attrs={'min': 0, 'max': 10}),
            'problem_identification': forms.NumberInput(attrs={'min': 0, 'max': 10}),
            'objectives_methodology': forms.NumberInput(attrs={'min': 0, 'max': 10}),
            'literature_survey': forms.NumberInput(attrs={'min': 0, 'max': 10}),
            'documentation': forms.NumberInput(attrs={'min': 0, 'max': 10}),
            'results': forms.NumberInput(attrs={'min': 0, 'max': 10}),
            'presentation_quality': forms.NumberInput(attrs={'min': 0, 'max': 10}),
            'communication_skills': forms.NumberInput(attrs={'min': 0, 'max': 10}),
            'technical_knowledge': forms.NumberInput(attrs={'min': 0, 'max': 10}),
            'individual_involvement': forms.NumberInput(attrs={'min': 0, 'max': 10}),
            'fundamentals_questions': forms.NumberInput(attrs={'min': 0, 'max': 10}),
            'clarity_in_answers': forms.NumberInput(attrs={'min': 0, 'max': 10}),
            'understanding_ability': forms.NumberInput(attrs={'min': 0, 'max': 10}),
            'attitude_towards_questions': forms.NumberInput(attrs={'min': 0, 'max': 10}),
        }