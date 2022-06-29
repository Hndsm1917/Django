import nvdlib
import datetime
import requests
# import pdfkit

from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, JsonResponse
from json import loads
from django.shortcuts import render
from django.template.loader import render_to_string

API_KEY = "07f6e22a-77bc-408d-94a4-f90f4ac12b08"



@require_http_methods(["GET"])
def index(request):
  HTML_STRING = render_to_string("index.html")
  return HttpResponse(HTML_STRING)



@require_http_methods(["GET"])
def info(request):
  HTML_STRING = render_to_string("info.html", {
    'info_arr': [
      'Добавь',
      'Тектс2',
      'Лы',
      'ся4',
    ]
  })

  return HttpResponse(HTML_STRING)



@require_http_methods(["GET"])
def get_all_cve(request):
  params = {"apiKey": API_KEY}
  resp = requests.get('https://services.nvd.nist.gov/rest/json/cves/1.0/', params = params)
  cve_page = resp.json()['result']

  return JsonResponse(cve_page, safe = False)



@require_http_methods(["GET"])
def get_new_cve(request):
  end = datetime.datetime.now()
  start = end - datetime.timedelta(days = 7)
  resp = nvdlib.searchCVE(pubStartDate = start, pubEndDate = end, key = API_KEY)
  res_list = [str(x) for x in resp]

  return JsonResponse({"result" : res_list}, safe = False) 



@require_http_methods(["GET"])
def get_critical_cve(request):
  resp = nvdlib.searchCVE(keyword = 'Microsoft Exchange', cvssV3Severity = 'Critical', key = API_KEY)
  res_list = [str(x) for x in resp]

  return JsonResponse({"result" : res_list}, safe = False) 
