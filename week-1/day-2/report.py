def grade_report(names: list[str], scores: list[int]) -> dict:
    report = dict(zip(names, scores))

    passed = {}
    for name, score in report.items():
        if score >= 80:
            passed[name] = score

    # average
    if not scores:
        average = 0.0
    else:
        average = round(sum(scores) / len(scores), 1)

    sorted_pairs = sorted(report.items(), key=lambda x: x[1], reverse=True)
    ranked = []
    for i, (name , score) in enumerate(sorted_pairs , start=1):
        ranked.append(f"{i}. {name} ({score})")
    

    return {"passed": passed, "average": average, "ranked": ranked}


result = grade_report(["ali", "sara", "bilal"], [85, 92, 78])
print(result)