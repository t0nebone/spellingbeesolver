from flask import Flask, render_template, request, escape
from spellingb import search_for_words_web

app = Flask(__name__)


@app.route('/spellingbsolver', methods=['POST'])
def do_search() -> str:
    strip = "[]"
    center_letter = request.form['center_letter'].lower()
    outside_letters = request.form['outside_letters'].lower()
    title = 'Spelling Bee Solved'
    results = str(search_for_words_web(center_letter, outside_letters)).strip(strip).replace("'", "")

    return render_template('results.html',
                           the_center_letter=center_letter,
                           the_outside_letters=outside_letters,
                           the_title=title,
                           the_results=results,
                           )


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title="NYT Spelling Bee Solver")


@app.route('/viewlog')
def view_the_log() -> str:
    contents = []
    with open('spellingb.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[0].append(line.strip("[\"ImmutableMultiDict([('center_letter','")[0])
                contents[1].append(
                    line.strip("[\"ImmutableMultiDict([('center_letter', 'b'), ('outside_letters', '")[:5])
                contents[-1].append(escape(item))

    titles = ('Center Leter', 'Outside Letter', 'Results')
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents, )


if __name__ == '__main__':
    app.run()
