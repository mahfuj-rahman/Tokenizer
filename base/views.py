from django.shortcuts import render, redirect
from .forms import FileForm
from analyzer.Buffer import Buffer
from analyzer.LexicalAnalyzer import LexicalAnalyzer
import collections
# Create your views here.
from .models import Files


def home(request):
    form = FileForm()
    data = Files.objects.all()

    context = {
        'form': form,
        'data': data
    }

    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'base/index.html', context)


def generate_table(request, fid):
    file = Files.objects.get(id=fid)
    # Lists for every list returned list from the function tokenize
    token = []
    lexeme = []
    row = []
    column = []
    length = 0
    buffer_obj = Buffer()
    analyzer_obj = LexicalAnalyzer()

    for i in buffer_obj.load_buffer(file='media/' + file.file.name):
        t, lex, lin, col = analyzer_obj.tokenize(i)
        token += t
        lexeme += lex
        row += lin
        column += col
        length += 1

    symbol_id = collections.Counter(lexeme)

    context = {
        'token': token,
        'lexeme': lexeme,
        'row': row,
        'col': column,
        'symbol_id': symbol_id,

    }

    return render(request, 'base/generate_table.html', context)
