from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # 用于 session

# 存储学生签到和分数
students = {}

# 老师账号密码
TEACHER_USERNAME = 'teacher'
TEACHER_PASSWORD = '123456'

# ------------------------------
# 学生签到页
# ------------------------------
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            if name not in students:
                students[name] = 0
            return render_template('success.html', name=name)
    return render_template('index.html', students=students)

# ------------------------------
# 老师登录页
# ------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == TEACHER_USERNAME and password == TEACHER_PASSWORD:
            session['teacher_logged_in'] = True
            return redirect(url_for('admin'))
        else:
            error = "Invalid username or password!"
    return render_template('login.html', error=error)

# ------------------------------
# 老师管理页（加减分 + 随机抽取）
# ------------------------------
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if not session.get('teacher_logged_in'):
        return redirect(url_for('login'))

    selected_student = None

    if request.method == 'POST':
        if 'student_name' in request.form:
            # 加减分操作
            name = request.form.get('student_name')
            action = request.form.get('action')
            if name in students:
                if action == 'add':
                    students[name] += 1
                elif action == 'subtract':
                    students[name] -= 1
        elif 'random_draw' in request.form:
            # 随机抽取学生
            if students:
                selected_student = random.choice(list(students.keys()))

        return render_template('admin.html', students=students, selected_student=selected_student)

    return render_template('admin.html', students=students, selected_student=selected_student)

# ------------------------------
# 老师登出
# ------------------------------
@app.route('/logout')
def logout():
    session.pop('teacher_logged_in', None)
    return redirect(url_for('login'))

# ------------------------------
if __name__ == '__main__':
    app.run(debug=True)
