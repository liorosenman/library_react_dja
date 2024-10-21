def extract_parameters_from_request(request):
    parameters = request.POST.dict() if request.method == 'POST' else request.GET.dict()
    return parameters