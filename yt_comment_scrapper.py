import http.client
import json

conn = http.client.HTTPSConnection("www.youtube.com")
payload = json.dumps({
  "context": {
    "client": {
      "userAgent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36,gzip(gfe)",
      "clientName": "WEB",
      "clientVersion": "2.20240111.00.00",
      "originalUrl": "https://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID",
      "platform": "DESKTOP",
      "configInfo": {
        "appInstallData": ""
      },
      "timeZone": "Asia/Jakarta",
      "acceptHeader": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
      "utcOffsetMinutes": 420,
      "connectionType": "CONN_CELLULAR_4G",
      "memoryTotalKbytes": "8000000",
      "mainAppWebInfo": {}
    },
    "user": {
      "lockedSafetyMode": False
    },
    "request": {
      "useSsl": True,
      "internalExperimentFlags": [],
      "consistencyTokenJars": []
    },
    "adSignalsInfo": {
      "params": [],
      "bid": "ANyPxKpYF59cvv5luG8sitIsThCxYlkWnO9THtElS_bH01LSjTDrc4rb0lgbydjn9BvGQVQn8Ds9XKLCFMiOGwQGWGns6kA8Rg"
    }
  },
  "continuation": "Eg0SC2M5YkhiQjh6N0NnGAYyOCIRIgtjOWJIYkI4ejdDZzAAeAIwAUIhZW5nYWdlbWVudC1wYW5lbC1jb21tZW50cy1zZWN0aW9u"
})
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/youtubei/v1/next?key=API_KEY_PUBLIC&prettyPrint=false", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
