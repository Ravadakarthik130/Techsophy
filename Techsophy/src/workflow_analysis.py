def compute_metrics(df):
    return {
        "avg_commits": df["commits"].mean(),
        "avg_pr_cycle_time": df["pr_cycle_time_days"].mean(),
        "avg_issues_resolved": df["issues_resolved"].mean(),
        "avg_deployment_frequency": df["deployment_frequency"].mean(),
        "avg_build_failure_rate": df["build_failure_rate"].mean(),
    }
