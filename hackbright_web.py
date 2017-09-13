"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template, redirect

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    test_github = hackbright.get_student_by_github(github)

    project_grades = hackbright.get_grades_by_github(github)

    if test_github is None:
        return redirect("/student-search")
    else:
        first, last, github = hackbright.get_student_by_github(github)

    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github,
                           project_grades=project_grades)

    return html


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/new-student")
def process_new_student():
    """Form for new students"""

    return render_template("new_student.html")


@app.route("/student-add", methods=['POST'])
def student_add():
    """Adds new student to table."""

    student_first = request.form.get('first_name')
    student_last = request.form.get('last_name')
    student_github = request.form.get('github_name')

    hackbright.make_new_student(student_first, student_last, student_github)

    return render_template("added_student.html", github=student_github)


@app.route("/project")
def project():

    title = request.args.get('project')

    print title

    # projects = hackbright.get_project_by_title(title)

    # return render_template("/project_info.html", projects=projects)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
