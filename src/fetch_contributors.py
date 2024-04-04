import requests

owner = "magdalenakuhn17"
repo = "awesome-cheap-llms"

# GitHub API URL for contributors
url = f"https://api.github.com/repos/{owner}/{repo}/contributors"

# Fetch the contributors
response = requests.get(url)
contributors = response.json()

# Prepare the markdown list of contributors
contributors_md = "\n".join([f"- [{c['login']}]({c['html_url']})" for c in contributors])

# Read the current README
with open("README.md", "r") as file:
    readme_contents = file.read()

# Append the contributors list to the README
readme_contents += "\n\n\n# Top :1st_place_medal: :2nd_place_medal: :3rd_place_medal: contributors \n" + contributors_md

# Write the updated contents back to the README
with open("README.md", "w") as file:
    file.write(readme_contents)
