#Task 1 — Process the Scores Write a function process_scores(students)

def process_scores(students):
    averages = {}

    for name, scores in students.items():
        avg = round(sum(scores) / len(scores), 2)
        averages[name] = avg

    return averages

#Task 2 — Classify the Grades Write a function classify_grades(averages)

def classify_grades(averages):

    classified = {}

    for name, avg in averages.items():
        if avg >= 90:
            grade = "A"
        elif avg >= 75:
            grade = "B"
        elif avg >= 60:
            grade = "C"
        else:
            grade = "F"

        classified[name] = (avg, grade)

    return classified

#Task 3 — Generate the Report Write a function generate_report(classified, passing_avg=70)

def generate_report(classified, passing_avg=70):
 
    print("===== Student Grade Report =====")

    total = len(classified)
    passed = 0

    for name, (avg, grade) in classified.items():
        status = "PASS" if avg >= passing_avg else "FAIL"

        if status == "PASS":
            passed += 1

        print(f"{name:<9} | Avg: {avg:>5.2f} | Grade: {grade} | Status: {status}")

    failed = total - passed

    print("================================")
    print(f"Total Students : {total}")
    print(f"Passed         : {passed}")
    print(f"Failed         : {failed}")

    return passed


# -------- Main Block --------
if __name__ == "__main__":

    students = {
        "Alice": [85, 88, 90, 82],
        "Bob": [60, 65, 58, 67],
        "Clara": [95, 97, 94, 99]
    }

    averages = process_scores(students)
    classified = classify_grades(averages)
    generate_report(classified)
	
"""	
Note: generate_report(classified, passing_avg=70) - Since the passing average is 70, any average below 70 will FAIL.
===== Student Grade Report =====
Alice     | Avg: 86.25 | Grade: B | Status: PASS
Bob       | Avg: 62.50 | Grade: C | Status: FAIL
Clara     | Avg: 96.25 | Grade: A | Status: PASS
================================
Total Students : 3
Passed         : 2
Failed         : 1
"""