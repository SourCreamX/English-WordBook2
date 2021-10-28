from flask import Flask, render_template, request, send_from_directory
import csv, random

app = Flask(__name__)
# 日本語の文字化けを防ぐ
app.config['JSON_AS_ASCII'] = False

@app.route("/", methods=['GET','POST'])
def setting():
    if request.method == 'POST':
        # chapterの選択
        if request.form.get('chapter') == 'all':
            word_list = []
            for i in range(1,8):
                chapter_pass = 'dict/chapter' + str(i) + '.csv'
                with open(chapter_pass) as f:
                    reader = csv.reader(f)      
                    word_list += [row for row in reader]
        else:
            chapter = request.form.get('chapter')
            chapter_dict = 'dict/chapter' + chapter + '.csv'
            with open(chapter_dict) as f:
                reader = csv.reader(f)  
                word_list = [row for row in reader]

        # 並び順の設定
        if request.form.get('sort') == 'random':
            random.shuffle(word_list)

        # 学習範囲の設定
        m1 = int(request.form.get('min'))-1
        m2 = int(request.form.get('max'))
        range_word_list = word_list[m1:m2]

        return render_template('check.html', word_list=range_word_list, dict_length=len(range_word_list))

    else:
        return render_template('setting.html')

@app.route("/pronunciation/<path:filename>")
def play(filename):
    return send_from_directory("pronunciation", filename)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)