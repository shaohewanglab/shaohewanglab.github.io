import os, argparse
import pandas as pd

def bib_to_html(bibFile=None):
    '''
    Convert bibliography list in BibTeX format into a list of text compatible with
    the publications section of this website

    Parameters
    ----------
        bibFile: the path to the bibliography file

    Output
    -------
        A html file with formatted list of publications
    '''
    if bibFile is None:
        bibFile = 'ShaoheWang_selected.bib'

    df = bib_to_df(bibFile)
    
    html_file = os.path.splitext(bibFile)[0]+'.html'
    with open(html_file, 'w') as writer:
        for i in range(len(df)):
            paper = '<p>' + \
                    df.author[i] + '.' + \
                    ' <a href="'+df.url[i]+'" target="_blank">'+df.title[i]+'</a>' + \
                    ' (' + str(df.year[i]) + ')' + \
                    ' <i>' + df.journal[i] + '</i>' + \
                    '</p>\n'
            writer.write(paper)

def bib_to_df(bibFile):
    '''
    Convert bibliography list in BibTeX format into a pandas data frame

    Parameters
    ----------
        bibFile: the path to the bibliography file

    Returns
    -------
        df: data frame containing selected bibliograpy data sorted by published year
    '''
    
    # Parse bibliography list
    bibList = open(bibFile, 'r').read()
    bibs = bibList.split('@article')[1:]
    
    titles = []
    authors = []
    journals = []
    years = []
    urls = []

    for bib in bibs:
        bibItems = bib.split('\n')
        for i in bibItems:
            if i.startswith('title'):
                title = i[len('title')+5:-3]
                titles.append(title)
            elif i.startswith('author'):
                author = i[len('author')+4:-2]
                author = reformat_author(author)
                authors.append(author)
            elif i.startswith('journal'):
                journal = i[len('journal')+4:-2]
                journals.append(journal)
            elif i.startswith('year'):
                year = i[len('year')+4:-1]
                years.append(year)
            elif i.startswith('url'):
                url = i[len('url')+4:-2]
                urls.append(url)
    
    # check to make sure every bib item has all the entries
    assert len(authors) == len(titles)
    assert len(journals) == len(titles)
    assert len(years) == len(titles)
    assert len(urls) == len(titles)

    # assemble into a pandas data frame to sort by year
    data = {'title': titles, 'author': authors, 'journal': journals, 'year': years, 'url': urls}
    df = pd.DataFrame(data)
    df.sort_values(by=['year'], ascending=False, inplace=True)
    
    return df

def reformat_author(author, team=None):
    '''
    '''
    if team is None:
        team = ['Wang, Shaohe', 'Wu, Di']
    authors = author.split(' and ')
    authorList = []
    for author in authors:    
        temp = author.split(', ') # split last name and first or middle names
        if author in team:
            # authorList.append('**' + temp[1] + ' ' + temp[0] + '**')
            authorList.append('<b>' + temp[1] + ' ' + temp[0] + '</b>')
        else:
            authorList.append(temp[1] + ' ' + temp[0])
    return ', '.join(authorList)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("bibFile", nargs='?', help="path to the bibliography file; default: ShaoheWang_selected.bib")

    args = parser.parse_args()
    bib_to_html(args.bibFile)
