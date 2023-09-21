
import requests
import json

class GetPrograms:
  # nstead of a specific class, we would instead have a class that retrieves JSON from any provided URL!

  def get_programs(self):
    # get_programs method is really just getting the response body from the requested URL, so we could name this get_response_body to be more accurate
    URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

    response = requests.get(URL)
    return response.content
  
  def program_school(self):
    # We could replace the custom program_school method with a general load_json method
    # we use the JSON library to parse the API response into nicely formatted JSON
    programs_list = []
    programs = json.loads(self.get_programs())
    for program in programs:
        programs_list.append(program["agency"])

    return programs_list


# programs = GetPrograms().get_programs()
# print(programs)

programs = GetPrograms()
programs_schools = programs.program_school()
# programs_schools = programs.get_response_body()

for school in set(programs_schools):
    print(school)
