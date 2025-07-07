def generate_recommendations(bottlenecks):
    suggestions = []
    for issue in bottlenecks:
        if "PR cycle" in issue:
            suggestions.append("Use automated code review and faster CI pipelines.")
        elif "commit" in issue:
            suggestions.append("Encourage smaller, more frequent commits.")
        elif "build failure" in issue:
            suggestions.append("Improve test coverage and CI reliability.")
        elif "deployment" in issue:
            suggestions.append("Automate deployments and adopt CI/CD.")
    return suggestions
