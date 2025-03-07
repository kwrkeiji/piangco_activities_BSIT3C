from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from django.core.files.uploadhandler import TemporaryFileUploadHandler
from django.http.multipartparser import MultiPartParser
import json

# In-memory storage for items
items = []

def find_item(item_id):
    return next((item for item in items if item['id'] == item_id), None)

def parse_json_request(request):
    try:
        return json.loads(request.body)
    except json.JSONDecodeError:
        return None

@csrf_exempt
@require_GET
def get_items(request):
    search_query = request.GET.get('search', '')
    filtered_items = [item for item in items if search_query.lower() in item['name'].lower()]
    return JsonResponse({'items': filtered_items if search_query else items}, status=200)

@csrf_exempt
@require_GET
def get_item(request, item_id):
    item = find_item(item_id)
    if item:
        return JsonResponse({'item': item}, status=200)
    return JsonResponse({'error': f'Item {item_id} not found'}, status=404)

@csrf_exempt
@require_POST
def add_item(request):
    name = None
    if request.content_type == 'application/json':
        data = parse_json_request(request)
        name = data.get('name') if data else None
    else:
        name = request.POST.get('name')

    if not name:
        return JsonResponse({'error': 'Name is required'}, status=400)

    new_item = {'id': len(items) + 1, 'name': name}
    items.append(new_item)
    return JsonResponse({'message': 'Item added', 'item': new_item}, status=201)

@csrf_exempt
@require_http_methods(["PUT"])
def update_item(request, item_id):
    item = find_item(item_id)
    if not item:
        return JsonResponse({'error': 'Item not found'}, status=404)

    name = None
    if request.content_type == 'application/json':
        data = parse_json_request(request)
        name = data.get('name') if data else None
    elif request.content_type.startswith('multipart/form-data'):
        request.upload_handlers = [TemporaryFileUploadHandler()]
        parser = MultiPartParser(request.META, request, request.upload_handlers)
        data, _ = parser.parse()
        name = data.get('name')

    if name:
        item['name'] = name
        return JsonResponse({'message': 'Item updated', 'item': item}, status=200)
    return JsonResponse({'error': 'No valid data provided'}, status=400)

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_item(request, item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return JsonResponse({'message': 'Item deleted'}, status=200)