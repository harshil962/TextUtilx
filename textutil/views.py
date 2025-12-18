from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', '')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    # ❌ If no option is selected
    if (removepunc == "off" and fullcaps == "off" and
        newlineremover == "off" and extraspaceremover == "off" and
        charcount == "off"):
        return render(request, 'error.html', {
            'error': 'Please select at least one option!'
        })

    analyzed = djtext
    purpose_list = []

    # ✅ Remove punctuation
    if removepunc == "on":
        punctuations = '''.,;:?!()[]{}<>/\|@#$%^&*_~=+-`'"'''
        analyzed = "".join(char for char in analyzed if char not in punctuations)
        purpose_list.append("Removed Punctuation")

    # ✅ Uppercase
    if fullcaps == "on":
        analyzed = analyzed.upper()
        purpose_list.append("Converted to Uppercase")

    # ✅ Remove extra spaces (safe)
    if extraspaceremover == "on":
        analyzed = " ".join(analyzed.split())
        purpose_list.append("Removed Extra Spaces")

    # ✅ Remove new lines
    if newlineremover == "on":
        analyzed = analyzed.replace("\n", "").replace("\r", "")
        purpose_list.append("Removed New Lines")

    # ✅ Character count
    if charcount == "on":
        count = len(analyzed)
        analyzed = f"Total Characters: {count}\n\n{analyzed}"
        purpose_list.append("Character Count")

    params = {
        'purpose': ", ".join(purpose_list),
        'analyzed_text': analyzed
    }

    return render(request, 'analyze.html', params)


def error(request):
    return render(request, 'error.html')
