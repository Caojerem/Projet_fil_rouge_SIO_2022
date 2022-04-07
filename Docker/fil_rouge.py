import arxiv
import urllib
import pdfx
import re
import spacy
from spacy.lang.fr.examples import sentences
from xml.sax.saxutils import escape
import sys

def after_references(mypdftext): 
    keyword1 = 'References'
    keyword2 = 'REFERENCES'
    keyword3 = 'R EFERENCES'
    keyword4 = 'Reference'
    keyword5='[1]' 

    if keyword1 in mypdftext :
            before_keyword, keyword, after_keyword = mypdftext.partition(keyword1)
    elif keyword2 in mypdftext :
            before_keyword, keyword, after_keyword = mypdftext.partition(keyword2)
    elif keyword3 in mypdftext :
            before_keyword, keyword, after_keyword = mypdftext.partition(keyword3)
    elif keyword4 in mypdftext :
            before_keyword, keyword, after_keyword = mypdftext.partition(keyword4)
    elif keyword5 in mypdftext :
            before_keyword, keyword, after_keyword = mypdftext.partition(keyword5)
    else:
        after_keyword = mypdftext[:10000]
    return after_keyword

def extract(text:str) :
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text.strip())
    named_entities = []
    
    for i in doc.ents:
        entry = str(i.lemma_).lower()
        text = text.replace(str(i).lower(), "")
        if i.label_ in ["PERSON"]:
            named_entities.append(entry.title().replace(" ", "_").replace("\n","_"))
        named_entities = list(dict.fromkeys(named_entities))
    return named_entities




def pdf_arxiv():
    search = arxiv.Search(
        query = "computer science &  ai",
        # id_list=["1605.08386v1"]
        max_results = 1,
        sort_by = arxiv.SortCriterion.SubmittedDate
    )

    for result in search.results():
        print ("Titre :", result.title)
        print ("Lien :", result.pdf_url)

    for result in search.results():
        author = result.authors
        author_list = [re.sub("[^A-Za-z0-9]","_",str(i)) for i in author]
    
    print("Autheurs :", author_list)

    response = urllib.request.urlopen(result.pdf_url)    
    file = open("Test" + ".pdf", 'wb')
    file.write(response.read())
    file.close()

    # Leture du PDF
    pdf = pdfx.PDFx("Test.pdf")
    metadata = pdf.get_metadata()
    references_dict = pdf.get_references_as_dict()
    text = pdf.get_text()
    
    return text

text=pdf_arxiv()
references = after_references(text)
references_list = extract(references)

print("5 premiers noms cités dans les références :", references_list[:5])