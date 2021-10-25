import requests

#otettu External IP pois ja laitettu tilalle example.com
r = requests.get("http://example.com/health.html")

print("Status:", r.status_code)

if r.status_code == 200:
  print("Kaikki on ok.")
else:
  print("Kaikki ei ole ok.")