import requests

def execute_sparql_query(query):
    """Executes a SPARQL query against Wikidata."""
    url = 'https://query.wikidata.org/sparql'
    headers = {
        'User-Agent': 'Scribe-Data/0.1 (https://github.com/scribe-org/Scribe-Data)',
        'Accept': 'application/json',
    }
    response = requests.get(url, headers=headers, params={'query': query})
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

def query_finnish_verbs():
    """Queries Finnish verbs from Wikidata."""
    query = """
    SELECT
      (REPLACE(STR(?lexeme), "http://www.wikidata.org/entity/", "") AS ?lexemeID)
      ?verb

    WHERE {
      ?lexeme dct:language wd:Q1412 ;  # Finnish language
        wikibase:lexicalCategory wd:Q24905 ;  # Verbs
        wikibase:lemma ?verb .
    }
    """
    result = execute_sparql_query(query)
    return result
