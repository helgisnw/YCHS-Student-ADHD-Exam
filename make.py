import requests
import getxl
from getxl import b
from openpyxl import load_workbook

def a():
    b()
    file = load_workbook("./result/data.xlsx", data_only=True)

    load_ws = file["설문지 응답 시트1"]


    results = []


    for i in range(100):
        index = i+2
        name = load_ws[f'B{index}'].value
        if name == None:
            continue
        anxiety = load_ws[f'W{index}': f'AI{index}']
        ADHD = load_ws[f'C{index}' : f'V{index}']
        ADHD_score = 0
        anxiety_score = 0
        for row in ADHD:
            for cell in row:
                if cell.value == None:
                    continue
                ADHD_score += int(cell.value)
        
        for row in anxiety:
            for cell in row:
                if cell.value == None:
                    continue
                anxiety_score += int(cell.value)


        results.append({
            "name": name,
            "ADHD": ADHD_score,
            "ANXIETY": anxiety_score
        })


    for result in results:
        with open(f"./result/{result['name']}.html", "w") as file:

            html = f"""
        <!DOCTYPE html>
        <html lang="ko">
        <head>
        <meta charset="UTF-8">
        <title>{result["name"]}님의 검사 결과</title>
        <link rel="stylesheet" href="style.css">
        </head>
        <body>
        <header class="center">
            <h1>{result["name"]}님의 검사 결과</h1>
        </header>
        <main class="center">
            <section class="student-info center">
            <h2>학생 정보</h2>
            <p class="name center">학번, 이름: <span>{ result["name"] }</span></p>
            </section>
            <section class="score center">
            <h2>검사 결과</h2>
            <ul>
                <li>ADHD 총 점수: <span>{ result["ADHD"] }</span></li>
                <li>공부 불안도 총 점수: <span>{ result["ANXIETY"] }</span></li>
            </ul>
            </section>
        </main>
        <footer class="center footer">
            <p>Made By <a href='https://github.com/helgisnw'>진우현</a>, Helped by <a href='https://github.com/dkqdkq'>김도엽</a></p>
        </footer>
        </body>
        </html>


        """
            file.write(html)
    