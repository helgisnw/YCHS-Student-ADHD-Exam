import requests
from openpyxl import load_workbook


file = load_workbook("./test.xlsx", data_only=True)

load_ws = file["설문지 응답 시트1"]

get_cells = load_ws['AP3':'AP1000']
get_names = load_ws['AK3':'AK1000']
get_anxiety = load_ws['AQ3' : 'AQ1000']


name = []
student_ADHD = []
exam_anxiety = []

for row in get_cells:
    for cell in row:
        print(cell.value)
        student_ADHD.append(cell.value)

for row in get_names:
    for cell in row:
        print(cell.value)
        name.append(cell.value)

for row in get_anxiety:
    for cell in row:
        print(cell.value)
        exam_anxiety.append(cell.value)


print(name)
print(student_ADHD)

for i in range(len(name)):
    #html = f"<html><head><meta charset=\"utf-8\"></head><body><h1>{str(name[i])}의 검사결과입니다.</h1><br>ADHD 총 점수는 {str(student_ADHD[i])}점 입니다!<br>공부 불안도 총 점수는{str(exam_anxiety[i])}점 입니다.</body></html>"
    html = f"""
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>{name[i]}님의 검사 결과</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header class="center">
    <h1>{name[i]}님의 검사 결과</h1>
  </header>
  <main class="center">
    <section class="student-info center">
      <h2>학생 정보</h2>
      <p class="name center">학번, 이름: <span>{ name[i] }</span></p>
    </section>
    <section class="score center">
      <h2>검사 결과</h2>
      <ul>
        <li>ADHD 총 점수: <span>{ student_ADHD[i] }</span></li>
        <li>공부 불안도 총 점수: <span>{ exam_anxiety[i] }</span></li>
      </ul>
    </section>
  </main>
  <footer class="center footer">
    <p>Copyright &copy;helgisnw 2023</p>
  </footer>
</body>
</html>


"""

# You can then use this 'html' variable as needed in your application.

    with open(f"/Project/html/result{name[i]}.html", 'w', encoding = 'utf-8') as file:
        file.write(html)
        
        
