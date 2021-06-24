from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homepage(request):
    resp = HttpResponse()
    resp["Link"] = "<style.css>; rel=stylesheet"
    resp["Refresh"] = "20; https://github.com/patrickgatiri"

    return resp


def cssstylesheet(request):

    css = """
        body { 
            display: block;
            background-image: url(https://media.giphy.com/media/TdfyKrN7HGTIY/giphy.gif);
            background-repeat: no-repeat;
            background-size: cover;
            color: red;
            text-align:center;
        }

        body::before {
            display: inline-block;
            padding-top: 3rem;
            content: "Ain't no view-source around here.";
        }
    """

    resp = HttpResponse(css)

    return resp
