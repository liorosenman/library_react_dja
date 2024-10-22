# def extract_parameters_from_request(request):
#     parameters = request.POST.dict() if request.method == 'POST' else request.GET.dict()
#     return parameters

def extract_parameters_from_request(request):
    return {
        'name': request.data.get('name'),
        'author': request.data.get('author'),
        'year_published': request.data.get('year_published'),
        'borrow_time': request.data.get('borrow_time'),
        'filename': request.data.get('filename'),
        'status': request.data.get('status')  # Optional, may default to 'available'
    }
