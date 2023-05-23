import requests

query_type = input("What do you want to find? for eg(brother/sister/father/): ")

if query_type == "brother":
    query = """
    SELECT ?brother WHERE {{
      ?brother <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.benchmark.org/family#Brother> .
    }}
    """
elif query_type == "sister":
    query = """
    SELECT ?sister WHERE {{
      ?sister <http://www.w3.org/1999/02/22-rdf-syntax-ns#type>  <http://www.benchmark.org/family#Sister> .
    }}
    """
elif query_type == "father":
    query = """
    SELECT ?father WHERE {{
      ?father <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.benchmark.org/family#Father> .
    }}
    """
elif query_type == "female":
    query = """
    SELECT ?female WHERE {{
      ?female <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.benchmark.org/family#Female> .
    }}
    """
elif query_type == "male":
    query = """
    SELECT ?male WHERE {{
      ?male <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.benchmark.org/family#Male> .
    }}
    """
elif query_type == "person":
    query = """
    SELECT ?person WHERE {{
      ?person <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.benchmark.org/family#Person> .
    }}
    """
elif query_type == "mother":
    query = """
    SELECT ?mother WHERE {{
      ?mother <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.benchmark.org/family#Mother> .
    }}
    """
elif query_type == "son":
    query = """
    SELECT ?son WHERE {{
      ?son <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.benchmark.org/family#Son> .
    }}
    """   
else:
    print("Invalid query type. Please choose either 'brother', 'sister', 'father'.'female','mother,'son','person'")
    exit()

response = requests.post('http://localhost:3030/family-benchmark_rich_background/sparql', data={'query': query})
results = [{query_type: '<'+i[query_type]['value']+'>'} for i in response.json()['results']['bindings']]
print(results)