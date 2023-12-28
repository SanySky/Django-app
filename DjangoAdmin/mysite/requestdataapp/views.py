from django.core.files.storage import FileSystemStorage
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render



def process_det_view(request: HttpRequest) -> HttpResponse:
    a = request.GET.get('a', '')
    b = request.GET.get('b', '')
    result = a + b
    context = {
        "a": a,
        "b": b,
        "result": result,
    }
    return render(request, "requestdataapp/request-query-params.html", context=context)


def user_form(request: HttpRequest) -> HttpResponse:
    return render(request, 'requestdataapp/user-bio-form.html')


def handle_file_upload(request: HttpRequest) -> HttpResponse:
    if request.method == "POST" and request.FILES.get("myfile"):
        myfile = request.FILES["myfile"]
        max_size = 100

        if myfile.size / 1024 > max_size:
            return HttpResponse(f"<h1>File size error!</h1>\n "
                                f"<h2>File bigger than {max_size} kb</h2>")

        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        print("saved file", filename)

    return render(request, 'requestdataapp/file-upload.html')
