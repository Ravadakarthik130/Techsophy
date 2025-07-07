def detect_bottlenecks(metrics):
    issues = []
    if metrics["avg_pr_cycle_time"] > 5:
        issues.append("High PR cycle time")
    if metrics["avg_commits"] < 6:
        issues.append("Low commit frequency")
    if metrics["avg_build_failure_rate"] > 0.1:
        issues.append("High build failure rate")
    if metrics["avg_deployment_frequency"] < 3:
        issues.append("Low deployment frequency")
    return issues
