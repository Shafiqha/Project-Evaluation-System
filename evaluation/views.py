from django.shortcuts import get_object_or_404, render, redirect
from .models import Student, Team, Evaluation
from .forms import TeamUploadForm, EvaluationForm

from django.shortcuts import render, redirect
from .models import Student, Team, Evaluation

def home(request):
    return render(request, 'evaluation/home.html')

def coordinator_dashboard(request):
    # Fetch all students for the form
    students = Student.objects.all()
    
    # Fetch all teams and their evaluations for display
    teams_with_evaluations = []
    teams = Team.objects.all()
    for team in teams:
        evaluations = Evaluation.objects.filter(team=team)
        
        # Initialize phase-wise marks and counts
        phase_marks = {'phase1': 0, 'phase2': 0, 'phase3': 0}
        phase_count = {'phase1': 0, 'phase2': 0, 'phase3': 0}
        total_marks = 0
        total_evaluations_count = 0

        # Collect evaluations and calculate marks
        for evaluation in evaluations:
            phase_marks[evaluation.phase] += evaluation.calculate_total_marks()
            phase_count[evaluation.phase] += 1
            total_marks += evaluation.calculate_total_marks()
            total_evaluations_count += 1

        # Calculate average marks for each phase
        phase_marks_avg = {
            'phase1': phase_marks['phase1'] / phase_count['phase1'] if phase_count['phase1'] else 0,
            'phase2': phase_marks['phase2'] / phase_count['phase2'] if phase_count['phase2'] else 0,
            'phase3': phase_marks['phase3'] / phase_count['phase3'] if phase_count['phase3'] else 0,
        }

        # Calculate total average marks across all phases
        total_avg_marks = (
            (phase_marks_avg['phase1'] + phase_marks_avg['phase2'] + phase_marks_avg['phase3']) / 3
            if total_evaluations_count
            else 0
        )

        # Add team data with evaluations to the list
        teams_with_evaluations.append({
            'team': team,
            'evaluations': evaluations,
            'phase_marks_avg': phase_marks_avg,
            'total_avg_marks': total_avg_marks,
        })

    # Handle POST requests
    if request.method == 'POST' and 'action' in request.POST:
        if request.POST['action'] == 'add_student':
            # Add a new student
            student_name = request.POST.get('name')
            new_student = Student.objects.create(name=student_name)
            new_student.save()
            return redirect('coordinator_dashboard')
        
        if request.POST['action'] == 'create_team':
            # Create a new team
            team_name = request.POST.get('team_name')
            guide_name = request.POST.get('guide_name', '')
            student_ids = request.POST.getlist('students')
            selected_students = Student.objects.filter(id__in=student_ids)

            new_team = Team.objects.create(name=team_name, guide_name=guide_name)
            new_team.students.set(selected_students)
            new_team.save()

            return redirect('coordinator_dashboard')

    # Render the coordinator dashboard with students and teams data
    return render(request, 'evaluation/coordinator_dashboard.html', {
        'teams_with_evaluations': teams_with_evaluations,
        'students': students,
    })
def team_dashboard(request, team_id):
    team = get_object_or_404(Team, id=team_id)

    # Fetch all evaluations for the team
    evaluations = team.evaluations.all()

    # Initialize phase-wise marks and evaluator details
    phase_marks = {'phase1': 0, 'phase2': 0, 'phase3': 0}
    phase_counts = {'phase1': 0, 'phase2': 0, 'phase3': 0}
    evaluators = {'phase1': set(), 'phase2': set(), 'phase3': set()}

    # Process evaluations
    for evaluation in evaluations:
        phase = evaluation.phase
        total_marks = evaluation.calculate_total_marks()
        phase_marks[phase] += total_marks
        phase_counts[phase] += 1
        evaluators[phase].add(evaluation.panelist_name)

    # Calculate average marks for each phase
    phase_avg = {
        phase: (phase_marks[phase] / phase_counts[phase] if phase_counts[phase] > 0 else 0)
        for phase in phase_marks
    }

    # Determine overall average marks
    total_average_marks = sum(phase_avg.values()) / 3 if evaluations.exists() else 0

    if request.method == "POST":
        form = TeamUploadForm(request.POST, request.FILES, instance=team)
        if form.is_valid():
            form.save()
    else:
        form = TeamUploadForm(instance=team)

    return render(request, 'evaluation/team_dashboard.html', {
        'team': team,
        'form': form,
        'phase_avg': phase_avg,
        'evaluators': evaluators,
        'total_average_marks': total_average_marks,
    })

def panelist_dashboard(request):
    teams = Team.objects.all()  # Fetch all teams
    if request.method == "POST":
        team_id = request.POST.get('team_id')
        team = Team.objects.get(id=team_id)
        form = EvaluationForm(request.POST)
        if form.is_valid():
            evaluation = form.save(commit=False)
            evaluation.team = team
            evaluation.panelist_name = request.POST.get('panelist_name')  # Add panelist name
            evaluation.save()
            # Update the team's average marks
            team.average_marks = evaluation.calculate_average()
            team.save()
    else:
        form = EvaluationForm()
    return render(request, 'evaluation/panelist_dashboard.html', {
        'teams': teams,
        'form': form,
        'rubrics': [
            "Abstract/Synopsis Write-up",
            "Selection of Topic/Relevance of the subject to discipline",
            "Problem Identification",
            "Objectives and Methodology",
            "Breadth of Literature Survey",
            "Documentation/Systematic Approach",
            "Results (inference, conclusions, etc.)",
            "Quality of preparation of presentation",
            "Communication Skills",
            "Technical knowledge and awareness",
            "Individual involvement",
            "Questions relating to fundamentals and concepts",
            "Clarity in answering questions",
            "Understanding ability of questions asked",
            "Attitude towards questions asked"
        ]
    })