import requests

inputType = input("Please Tell What to find? Like brother/sister/father/ : ")

if inputType == "brother":
    query = """
    SELECT ?brother WHERE {{
      ?brother <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.benchmark.org/family#Brother> .
    }}
    """
elif inputType == "sister":
    query = """
    SELECT ?sister WHERE {{
      ?sister <http://www.w3.org/1999/02/22-rdf-syntax-ns#type>  <http://www.benchmark.org/family#Sister> .
    }}
    """
elif inputType == "father":
    query = """
    SELECT ?father WHERE {{
      ?father <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.benchmark.org/family#Father> .
    }}
    """
elif inputType == "female":
    query = """
    SELECT ?female WHERE {{
      ?female <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.benchmark.org/family#Female> .
    }}
    """
elif inputType == "male":
    query = """
    SELECT ?male WHERE {{
      ?male <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.benchmark.org/family#Male> .
    }}
    """
elif inputType == "person":
    query = """
    SELECT ?person WHERE {{
      ?person <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.benchmark.org/family#Person> .
    }}
    """
elif inputType == "mother":
    query = """
    SELECT ?mother WHERE {{
      ?mother <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.benchmark.org/family#Mother> .
    }}
    """
elif inputType == "son":
    query = """
    SELECT ?son WHERE {{
      ?son <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.benchmark.org/family#Son> .
    }}
    """   
else:
    print("Invalid query, Please you chose either /brother/sister/father/female/mother/son/person")
    exit()

res = requests.post('http://localhost:3030/family-benchmark_rich_background/sparql', data={'query': query})
result = [{inputType: '<'+i[inputType]['value']+'>'} for i in res.json()['results']['bindings']]
print('here is the Result',result)