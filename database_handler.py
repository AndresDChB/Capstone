import psycopg2
from pyalex import Works
from work_parse_utils import *

def connect_to_db():
    return psycopg2.connect(host='localhost', dbname = 'postgres', user='postgres', password='admin',port=5432)

def insert_paper_metadata(works):
    conn = connect_to_db
    cur = conn.cursor()

    for work in works:
        openalex_id = strip_openalex_id(work['id'])
        title = work['title']
        authors = get_authors_and_ids(work)
        year = work['publication_year']
        pdf_link = work.get('open_access', {}).get('oa_url')
        abstract = work['abstract']

        #todo define query
        cur.execute("""
        INSERT
                    """)

    conn.commit()

    cur.close()
    conn.close()