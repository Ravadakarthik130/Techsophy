from src.data_loader import load_metrics
from src.workflow_analysis import compute_metrics
from src.bottleneck_detector import detect_bottlenecks
from src.recommender import generate_recommendations

def main():
    df = load_metrics("data/dev_metrics.csv")
    metrics = compute_metrics(df)
    bottlenecks = detect_bottlenecks(metrics)
    recommendations = generate_recommendations(bottlenecks)

    print("\n=== Productivity Metrics ===")
    for key, value in metrics.items():
        print(f"{key}: {value:.2f}")

    print("\n=== Detected Bottlenecks ===")
    for issue in bottlenecks:
        print(f"- {issue}")

    print("\n=== Suggested Improvements ===")
    for rec in recommendations:
        print(f"- {rec}")

if __name__ == "__main__":
    main()
