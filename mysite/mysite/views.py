# import nvdlib
# import datetime
# import requests
# import pdfkit

from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, JsonResponse
from json import loads
from django.shortcuts import render

from django.template.loader import render_to_string

info_arr = [
  'Добавь',
  'Тектс2',
  'Лы',
  'ся4',
]

API_KEY = ""

@require_http_methods(["GET"])
def info(request):
  HTML_STRING = render_to_string("info.html", {
    'info_arr': info_arr
  })
  return HttpResponse(HTML_STRING)

# @require_http_methods(["GET"])
# def get_all_cve(request):
#     params = {"apiKey": API_KEY}
#     resp = request.get("", params = params)
#     cve_page = resp.json()['result']

#     return JsonResponse(cve_page, safe = False)